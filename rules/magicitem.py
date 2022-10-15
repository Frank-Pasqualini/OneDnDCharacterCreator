"""
A magic item.
TODO
"""

from abc import ABC

from rules.common import validate_string


class MagicItem(ABC):
    """
    A magic item.
    TODO
    """

    _name: str
    _description: str

    def __init__(self,
                 name: str,
                 description: str):
        self._name = validate_string(name)
        self._description = validate_string(description)

    def __str__(self) -> str:
        return f"{self._name}. {self._description}"
