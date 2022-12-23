"""
A Species for a character.
"""

from __future__ import annotations

from abc import ABC

from rules import feats
from rules.common import validate_string
from rules.enums import CreatureTypes, Sizes


class Species(ABC):
    """
    A Species for a character.
    """

    _name: str
    _features: list[feats.Feat]
    _creature_type: CreatureTypes
    _size: Sizes
    _speed: int
    _life_span: int

    def __init__(self,
                 name: str,
                 features: list[feats.Feat],
                 creature_type: CreatureTypes = CreatureTypes.HUMANOID,
                 size: Sizes = Sizes.MEDIUM,
                 speed: int = 30,
                 life_span: int = 100):
        if speed < 0:
            raise Exception("A Species cannot have a negative speed")

        if life_span < 0:
            raise Exception("A Species cannot have a negative life span")

        self._name = validate_string(name)
        self._creature_type = creature_type
        self._size = size
        self._speed = speed
        self._life_span = life_span
        self._features = features

    def get_features(self) -> list[feats.Feat]:
        return self._features

    def get_name(self) -> str:
        return self._name

    def get_speed(self) -> int:
        return self._speed

    def half_species(self, name: str, other_life_span: int) -> Species:
        return Species(name=name,
                       features=self._features,
                       creature_type=self._creature_type,
                       size=self._size,
                       speed=self._speed,
                       life_span=int((self._life_span + other_life_span) // 2))

    def __str__(self) -> str:
        output = f"{self._name} Traits\n"

        output += f"Creature Type: {self._creature_type.value}\n"

        output += f"Size: {self._size.value}\n"

        output += f"Speed: {self._speed} feet\n"

        output += f"Lifespan: {self._life_span} years on average\n"

        output += f"As a{'n' if self._name[0].upper() in ['A', 'E', 'I', 'O', 'I'] else ''} {self._name}, you have"
        output += "these special traits."

        for feat in self._features:
            output += f"\n{feat.summary()}"

        return output
