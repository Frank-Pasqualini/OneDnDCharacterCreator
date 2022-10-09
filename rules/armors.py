"""
An armor item that modifies AC.
"""

from rules.common import validate_string
from rules.enums import ArmorTraining


class Armor:
    """
    An armor item that modifies AC.
    """

    _name: str
    _training_needed: ArmorTraining
    _armor_class: int
    _stealth_disadvantage: bool
    _strength_requirement: int

    def __init__(self,
                 name: str,
                 training_needed: ArmorTraining,
                 armor_class: int,
                 stealth_disadvantage: bool = False,
                 strength_requirement: int = 0):
        self._name = validate_string(name)
        self._training_needed = training_needed
        self._armor_class = armor_class
        self._stealth_disadvantage = stealth_disadvantage
        self._strength_requirement = strength_requirement

    def get_armor_class(self, dex_mod: int = 0) -> int:
        if self._training_needed == ArmorTraining.LIGHT:
            return self._armor_class + dex_mod
        if self._training_needed == ArmorTraining.MEDIUM:
            return self._armor_class + min(2, dex_mod)

        return self._armor_class
