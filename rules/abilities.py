"""
The set of 6 standard ability scores.
"""

from __future__ import annotations

import math


class Abilities:
    """
    The set of 6 standard ability scores.
    """

    _strength: int
    _dexterity: int
    _constitution: int
    _intelligence: int
    _wisdom: int
    _charisma: int

    def __init__(self,
                 strength: int = 0,
                 dexterity: int = 0,
                 constitution: int = 0,
                 intelligence: int = 0,
                 wisdom: int = 0,
                 charisma: int = 0):
        self._strength = strength
        self._dexterity = dexterity
        self._constitution = constitution
        self._intelligence = intelligence
        self._wisdom = wisdom
        self._charisma = charisma

    def get_strength(self) -> int:
        return self._strength

    def get_dexterity(self) -> int:
        return self._dexterity

    def get_constitution(self) -> int:
        return self._constitution

    def get_intelligence(self) -> int:
        return self._intelligence

    def get_wisdom(self) -> int:
        return self._wisdom

    def get_charisma(self) -> int:
        return self._charisma

    def get_strength_mod(self) -> int:
        return math.floor((self._strength - 10) / 2)

    def get_dexterity_mod(self) -> int:
        return math.floor((self._dexterity - 10) / 2)

    def get_constitution_mod(self) -> int:
        return math.floor((self._constitution - 10) / 2)

    def get_intelligence_mod(self) -> int:
        return math.floor((self._intelligence - 10) / 2)

    def get_wisdom_mod(self) -> int:
        return math.floor((self._wisdom - 10) / 2)

    def get_charisma_mod(self) -> int:
        return math.floor((self._charisma - 10) / 2)

    def __add__(self, other: Abilities) -> Abilities:
        return Abilities(strength=min(self._strength + other.get_strength(), 20),
                         dexterity=min(self._dexterity +
                                       other.get_dexterity(), 20),
                         constitution=min(self._constitution +
                                          other.get_constitution(), 20),
                         intelligence=min(self._intelligence +
                                          other.get_intelligence(), 20),
                         wisdom=min(self._wisdom + other.get_wisdom(), 20),
                         charisma=min(self._charisma + other.get_charisma(), 20))
