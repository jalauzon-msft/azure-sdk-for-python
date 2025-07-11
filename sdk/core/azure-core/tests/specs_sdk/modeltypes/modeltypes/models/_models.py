# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Dict, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .._utils.model_base import Model as _Model, rest_discriminator, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class ClientNameAndJsonEncodedNameModel(_Model):
    """Model with a property that has a client name.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: str
    """

    client_name: str = rest_field(name="wireName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Element(_Model):
    """Element.

    :ivar recursive_element:
    :vartype recursive_element: list[~modeltypes.models.RecursiveElement]
    """

    recursive_element: Optional[List["_models.RecursiveElement"]] = rest_field(
        name="recursiveElement", visibility=["read", "create", "update", "delete", "query"]
    )

    @overload
    def __init__(
        self,
        *,
        recursive_element: Optional[List["_models.RecursiveElement"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Fish(_Model):
    """This is base model for polymorphic multiple levels inheritance with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Salmon, Shark

    :ivar kind: Discriminator property for Fish. Required. Default value is None.
    :vartype kind: str
    :ivar age: Required.
    :vartype age: int
    """

    __mapping__: Dict[str, _Model] = {}
    kind: str = rest_discriminator(name="kind")
    """Discriminator property for Fish. Required. Default value is None."""
    age: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FlattenModel(_Model):
    """Model with one level of flattening.

    :ivar name: Required.
    :vartype name: str
    :ivar properties: Required.
    :vartype properties: ~modeltypes.models.PropertiesModel
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    properties: "_models.PropertiesModel" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    __flattened_items = ["description", "age"]

    @overload
    def __init__(
        self,
        *,
        name: str,
        properties: "_models.PropertiesModel",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        _flattened_input = {k: kwargs.pop(k) for k in kwargs.keys() & self.__flattened_items}
        super().__init__(*args, **kwargs)
        for k, v in _flattened_input.items():
            setattr(self, k, v)

    def __getattr__(self, name: str) -> Any:
        if name in self.__flattened_items:
            if self.properties is None:
                return None
            return getattr(self.properties, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__flattened_items:
            if self.properties is None:
                self.properties = self._attr_to_rest_field["properties"]._class_type()
            setattr(self.properties, key, value)
        else:
            super().__setattr__(key, value)


class Shark(Fish, discriminator="shark"):
    """The second level model in polymorphic multiple levels inheritance and it defines a new
    discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    GoblinShark, SawShark

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar shark_type: Required. Default value is None.
    :vartype shark_type: str
    """

    __mapping__: Dict[str, _Model] = {}
    kind: Literal["shark"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"shark\"."""
    shark_type: str = rest_discriminator(name="sharkType", visibility=["read", "create", "update", "delete", "query"])
    """Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        age: int,
        shark_type: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="shark", **kwargs)


class GoblinShark(Shark, discriminator="goblin"):
    """The third level model GoblinShark in polymorphic multiple levels inheritance.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar shark_type: Required. Default value is "goblin".
    :vartype shark_type: str
    """

    __mapping__: Dict[str, _Model] = {}
    shark_type: Literal["goblin"] = rest_discriminator(name="sharkType", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"goblin\"."""

    @overload
    def __init__(
        self,
        *,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, shark_type="goblin", **kwargs)


class PropertiesModel(_Model):
    """Properties model.

    :ivar description: Required.
    :vartype description: str
    :ivar age: Required.
    :vartype age: int
    """

    description: str = rest_field(name="modelDescription", visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    age: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        description: str,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ReadonlyModel(_Model):
    """Model with a readonly property.

    :ivar id: Required.
    :vartype id: int
    """

    id: int = rest_field(visibility=["read"])
    """Required."""


class RecursiveElement(Element):
    """RecursiveElement.

    :ivar level: Required.
    :vartype level: int
    """

    level: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        level: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Salmon(Fish, discriminator="salmon"):
    """The second level model in polymorphic multiple levels inheritance which contains references to
    other polymorphic instances.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "salmon".
    :vartype kind: str
    :ivar friends:
    :vartype friends: list[~modeltypes.models.Fish]
    :ivar hate:
    :vartype hate: dict[str, ~modeltypes.models.Fish]
    :ivar life_partner:
    :vartype life_partner: ~modeltypes.models.Fish
    """

    kind: Literal["salmon"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"salmon\"."""
    friends: Optional[List["_models.Fish"]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    hate: Optional[Dict[str, "_models.Fish"]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    life_partner: Optional["_models.Fish"] = rest_field(
        name="lifePartner", visibility=["read", "create", "update", "delete", "query"]
    )

    @overload
    def __init__(
        self,
        *,
        age: int,
        friends: Optional[List["_models.Fish"]] = None,
        hate: Optional[Dict[str, "_models.Fish"]] = None,
        life_partner: Optional["_models.Fish"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="salmon", **kwargs)


class SawShark(Shark, discriminator="saw"):
    """The third level model SawShark in polymorphic multiple levels inheritance.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar shark_type: Required. Default value is "saw".
    :vartype shark_type: str
    """

    __mapping__: Dict[str, _Model] = {}
    shark_type: Literal["saw"] = rest_discriminator(name="sharkType", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"saw\"."""

    @overload
    def __init__(
        self,
        *,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, shark_type="saw", **kwargs)


class Scratch(_Model):
    """A scratch model for testing purposes.

    :ivar prop: A string property. Required.
    :vartype prop: str
    """

    prop: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """A string property. Required."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
