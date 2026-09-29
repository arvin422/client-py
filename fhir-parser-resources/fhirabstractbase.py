#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for all FHIR elements.

from __future__ import annotations

from typing import TypeAlias

from .fhirdate import FHIRDate
import logging

logger = logging.getLogger(__name__)

JSONValue: TypeAlias = (
    str | int | float | bool | None
    | list["JSONValue"] | dict[str, "JSONValue"]
)
FHIRProperty: TypeAlias = tuple[str, str, type["FHIRAbstractBase | FHIRDate | str | int | float | bool"], bool, str | None, bool]


class FHIRValidationError(Exception):
    """ Exception raised when one or more errors occurred during model
    validation.
    """
    
    def __init__(self, errors, path=None):
        """ Initializer.
        
        :param errors: List of Exception instances. Also accepts a string,
            which is converted to a TypeError.
        :param str path: The property path on the object where errors occurred
        """
        if not isinstance(errors, list):
            errors = [TypeError(errors)]
        msgs = "\n  ".join([str(e).replace("\n", "\n  ") for e in errors])
        message = "{}:\n  {}".format(path or "{root}", msgs)
        
        super(FHIRValidationError, self).__init__(message)
        
        self.errors = errors
        """ A list of validation errors encountered. Typically contains
        TypeError, KeyError, possibly AttributeError and others. """
        
        self.path = path
        """ The path on the object where the errors occurred. """
    
    def prefixed(self, path_prefix):
        """ Creates a new instance of the receiver, with the given path prefix
        applied. """
        path = '{}.{}'.format(path_prefix, self.path) if self.path is not None else path_prefix
        return self.__class__(self.errors, path)


class FHIRAbstractBase(object):
    """ Abstract base class for all FHIR elements.
    """
    
    def __init__(self, jsondict: dict[str, JSONValue] | None = None, strict: bool = True) -> None:
        """ Initializer. If strict is true, raises on errors, otherwise uses
        `logger.warning()`.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self._primitive_extensions: dict[str, JSONValue] = {}
        self._resolved = None
        """ Dictionary of resolved resources. """
        
        self._owner = None
        """ Points to the parent resource, if there is one. """
        
        if jsondict is not None:
            if strict:
                self.update_with_json(jsondict)
            else:
                try:
                    self.update_with_json(jsondict)
                except FHIRValidationError as e:
                    for err in e.errors:
                        logger.warning(err)
    
    
    # MARK: Instantiation from JSON
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Initialize an element from a JSON dictionary or array.
        
        If the JSON dictionary has a "resourceType" entry and the specified
        resource type is not the receiving classes type, uses
        `FHIRElementFactory` to return a correct class instance.
        
        :raises: TypeError on anything but dict or list of dicts
        :raises: FHIRValidationError if instantiation fails
        :param jsonobj: A dict or list of dicts to instantiate from
        :returns: An instance or a list of instances created from JSON data
        """
        if isinstance(jsonobj, dict):
            return cls._with_json_dict(jsonobj)
        
        if isinstance(jsonobj, list):
            arr = []
            for jsondict in jsonobj:
                try:
                    arr.append(cls._with_json_dict(jsondict))
                except FHIRValidationError as e:
                    raise e.prefixed(str(len(arr)))
            return arr
        
        raise TypeError("`with_json()` on {} only takes dict or list of dict, but you provided {}"
            .format(cls, type(jsonobj)))
    
    @classmethod
    def _with_json_dict(cls, jsondict):
        """ Internal method to instantiate from JSON dictionary.
        
        :raises: TypeError on anything but dict
        :raises: FHIRValidationError if instantiation fails
        :returns: An instance created from dictionary data
        """
        if not isinstance(jsondict, dict):
            raise TypeError("Can only use `_with_json_dict()` on {} with a dictionary, got {}"
                .format(type(self), type(jsondict)))
        return cls(jsondict)
    
    @classmethod
    def with_json_and_owner(cls, jsonobj, owner):
        """ Instantiates by forwarding to `with_json()`, then remembers the
        "owner" of the instantiated elements. The "owner" is the resource
        containing the receiver and is used to resolve contained resources.
        
        :raises: TypeError on anything but dict or list of dicts
        :raises: FHIRValidationError if instantiation fails
        :param dict jsonobj: Decoded JSON dictionary (or list thereof)
        :param FHIRElement owner: The owning parent
        :returns: An instance or a list of instances created from JSON data
        """
        instance = cls.with_json(jsonobj)
        if isinstance(instance, list):
            for inst in instance:
                inst._owner = owner
        else:
            instance._owner = owner
        
        return instance
    
    
    # MARK: (De)Serialization
    
    def elementProperties(self) -> list[FHIRProperty]:
        """ Returns a list of tuples, one tuple for each property that should
        be serialized, as: ("name", "json_name", type, is_list, "of_many", not_optional)
        """
        return []
    
    def update_with_json(self, jsondict: dict[str, JSONValue] | None) -> None:
        """ Update the receiver with data in a JSON dictionary.
        
        :raises: FHIRValidationError on validation errors
        :param dict jsondict: The JSON dictionary to use to update the receiver
        :returns: None on success, a list of errors if there were errors
        """
        if jsondict is None:
            return
        
        if not isinstance(jsondict, dict):
            raise FHIRValidationError("Non-dict type {} fed to `update_with_json` on {}"
                .format(type(jsondict), type(self)))
        
        # loop all registered properties and instantiate
        errs = []
        valid = set(['resourceType'])   # used to also contain `fhir_comments` until STU-3
        found = {name[1:] for name in self._primitive_extensions}
        nonoptionals = set()
        for name, jsname, typ, is_list, of_many, not_optional in self.elementProperties():
            valid.add(jsname)
            
            # bring the value in shape
            err = None
            value = jsondict.get(jsname)
            if value is not None and hasattr(typ, 'with_json_and_owner'):
                try:
                    value = (
                        [None if item is None else typ.with_json_and_owner(item, self) for item in value]
                        if isinstance(value, list) and None in value
                        else typ.with_json_and_owner(value, self)
                    )
                except Exception as e:
                    value = None
                    err = e
            
            # got a value, test if it is of required type and assign
            if value is not None:
                if is_list and not isinstance(value, list):
                    err = TypeError('Expecting a list for property "{}"'.format(name))
                else:
                    items = value if is_list else [value]
                    primitive = typ in (str, int, float, bool) or issubclass(typ, FHIRDate)
                    details = jsondict.get('_' + jsname)
                    for index, item in enumerate(items):
                        if item is None and not (
                            primitive and is_list and isinstance(details, list)
                            and index < len(details) and details[index] is not None
                        ):
                            err = TypeError('Null property "{}" requires a primitive extension'.format(name))
                            break
                        if not self._matches_type(item, typ):
                            err = TypeError('Wrong type {} for property "{}", expecting {}'.format(type(item), name, typ))
                            break
                    if err is None:
                        setattr(self, name, value)
                    if items:
                        found.add(jsname)
                        if of_many is not None:
                            found.add(of_many)
                    elif not_optional:
                        nonoptionals.add(of_many or jsname)

            # not optional and missing, report (we clean `of_many` later on)
            elif not_optional:
                nonoptionals.add(of_many or jsname)
            
            _jsname = '_' + jsname
            _value = jsondict.get(_jsname)
            if _value is not None:
                valid.add(_jsname)
                try:
                    if typ not in (str, int, float, bool) and not issubclass(typ, FHIRDate):
                        raise TypeError('Only primitives support sibling extensions')
                    from .element import Element
                    if is_list:
                        if not isinstance(_value, list) or not _value:
                            raise TypeError('Primitive array extensions require a nonempty array')
                        extensions = [None if item is None else Element(item).as_json() for item in _value]
                        if not any(item is not None for item in extensions):
                            raise TypeError('Primitive extensions cannot be entirely null')
                        if isinstance(value, list) and len(value) != len(extensions):
                            raise TypeError('Primitive values and extensions must align')
                        self._primitive_extensions[_jsname] = extensions
                    else:
                        if not isinstance(_value, dict) or not _value:
                            raise TypeError('Primitive extension requires an element')
                        self._primitive_extensions[_jsname] = Element(_value).as_json()
                    found.add(of_many or jsname)
                except (TypeError, ValueError, FHIRValidationError) as error:
                    err = error

            # report errors
            if err is not None:
                errs.append(err.prefixed(name) if isinstance(err, FHIRValidationError) else FHIRValidationError([err], name))
        
        errs.extend(self._structure_errors(jsondict))

        # were there missing non-optional entries?
        if len(nonoptionals) > 0:
            for miss in nonoptionals - found:
                errs.append(KeyError("Non-optional property \"{}\" on {} is missing"
                    .format(miss, self)))
        
        # were there superfluous dictionary keys?
        if len(set(jsondict.keys()) - valid) > 0:
            for supflu in set(jsondict.keys()) - valid:
                errs.append(AttributeError("Superfluous entry \"{}\" in data for {}"
                    .format(supflu, self)))
        
        if len(errs) > 0:
            raise FHIRValidationError(errs)
    
    def as_json(self) -> dict[str, JSONValue]:
        """ Serializes to JSON by inspecting `elementProperties()` and creating
        a JSON dictionary of all registered properties. Checks:
        
        - whether required properties are not None (and lists not empty)
        - whether not-None properties are of the correct type
        
        :raises: FHIRValidationError if properties have the wrong type or if
            required properties are empty
        :returns: A validated dict object that can be JSON serialized
        """
        js: dict[str, JSONValue] = dict(self._primitive_extensions)
        errs = []
        
        # JSONify all registered properties
        found = set()
        nonoptionals = set()
        for name, jsname, typ, is_list, of_many, not_optional in self.elementProperties():
            if not_optional:
                nonoptionals.add(of_many or jsname)
            
            err = None
            value = getattr(self, name)
            if '_' + jsname in self._primitive_extensions:
                found.add(of_many or jsname)
            if value is None:
                continue
            
            if is_list:
                if not isinstance(value, list):
                   err = TypeError("Expecting property \"{}\" on {} to be list, but is {}"
                       .format(name, type(self), type(value)))
                elif len(value) > 0:
                    if any(not self._matches_type(item, typ) for item in value):
                        err = TypeError("Expecting property \"{}\" on {} to be {}, but is {}"
                            .format(name, type(self), typ, type(value[0])))
                    else:
                        lst = []
                        for v in value:
                            try:
                                lst.append(v.as_json() if hasattr(v, 'as_json') else v)
                            except FHIRValidationError as e:
                                err = e.prefixed(str(len(lst))).prefixed(name)
                        found.add(of_many or jsname)
                        js[jsname] = lst
            else:
                if not self._matches_type(value, typ):
                    err = TypeError("Expecting property \"{}\" on {} to be {}, but is {}"
                        .format(name, type(self), typ, type(value)))
                else:
                    try:
                        found.add(of_many or jsname)
                        js[jsname] = value.as_json() if hasattr(value, 'as_json') else value
                    except FHIRValidationError as e:
                        err = e.prefixed(name)
            
            if err is not None:
                errs.append(err if isinstance(err, FHIRValidationError) else FHIRValidationError([err], name))
        
        errs.extend(self._structure_errors(js))

        # any missing non-optionals?
        if len(nonoptionals - found) > 0:
            for nonop in nonoptionals - found:
                errs.append(KeyError("Property \"{}\" on {} is not optional, you must provide a value for it"
                    .format(nonop, self)))
        
        if len(errs) > 0:
            raise FHIRValidationError(errs)
        return js
    
    def _structure_errors(self, values: dict[str, JSONValue]) -> list[ValueError]:
        selected: dict[str, str] = {}
        errors: list[ValueError] = []
        for name, json_name, kind, is_list, group, required in self.elementProperties():
            value = values.get(json_name)
            details = values.get('_' + json_name)
            if is_list and isinstance(value, list):
                if isinstance(details, list) and len(details) != len(value):
                    errors.append(ValueError('Primitive values and extensions must align'))
                for index, item in enumerate(value):
                    if item is None and not (
                        isinstance(details, list) and index < len(details)
                        and details[index] is not None
                    ):
                        errors.append(ValueError('Null array entries require primitive extensions'))
            if group is None or (
                values.get(json_name) is None
                and values.get('_' + json_name) is None
            ):
                continue
            if group in selected:
                errors.append(ValueError('Conflicting properties "{}" and "{}" for choice "{}"'.format(selected[group], json_name, group)))
            selected[group] = json_name
        return errors

    def _matches_type(self, value, typ) -> bool:
        if value is None:
            return True
        if typ is int:
            return type(value) is int
        if typ is float:
            return type(value) in (int, float)
        return isinstance(value, typ)

    # MARK: Handling References
    
    def owningResource(self):
        """ Walks the owner hierarchy and returns the next parent that is a
        `DomainResource` instance.
        """
        owner = self._owner
        while owner is not None and not hasattr(owner, "contained"):
            owner = owner._owner
        return owner
    
    def owningBundle(self):
        """ Walks the owner hierarchy and returns the next parent that is a
        `Bundle` instance.
        """
        owner = self._owner
        while owner is not None and not 'Bundle' == owner.resource_type:
            owner = owner._owner
        return owner
    
    def resolvedReference(self, refid):
        """ Returns the resolved reference with the given id, if it has been
        resolved already. If it hasn't, forwards the call to its owner if it
        has one.
        
        You should probably use `resolve()` on the `FHIRReference` itself.
        
        :param refid: The id of the resource to resolve
        :returns: An instance of `Resource`, if it was found
        """
        if self._resolved and refid in self._resolved:
            return self._resolved[refid]
        return self._owner.resolvedReference(refid) if self._owner is not None else None
    
    def didResolveReference(self, refid, resolved):
        """ Called by `FHIRResource` when it resolves a reference. Stores the
        resolved reference into the `_resolved` dictionary.
        
        :param refid: The id of the resource that was resolved
        :param refid: The resolved resource, ready to be cached
        """
        if self._resolved is not None:
            self._resolved[refid] = resolved
        else:
            self._resolved = {refid: resolved}

