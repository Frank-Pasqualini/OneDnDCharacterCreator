from __future__ import annotations


class Abilities:
    """The set of 6 standard ability scores."""

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
        """Init a set of abilities."""

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

    def __add__(self, other: Abilities) -> Abilities:
        return Abilities(strength=self._strength + other.get_strength(),
                         dexterity=self._dexterity + other.get_dexterity(),
                         constitution=self._constitution + other.get_constitution(),
                         intelligence=self._intelligence + other.get_intelligence(),
                         wisdom=self._wisdom + other.get_wisdom(),
                         charisma=self._charisma + other.get_charisma())
