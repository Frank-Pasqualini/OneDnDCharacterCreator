from rules import feats
from rules.common import validate_string
from rules.enums import CreatureTypes, Sizes


class Race:
    """A Race for a character."""

    _name: str
    _creature_type: CreatureTypes
    _size: Sizes
    _speed: int
    _life_span: int
    _features: list[feats]

    def __init__(self,
                 name: str,
                 features: list[feats],
                 creature_type: CreatureTypes = CreatureTypes.HUMANOID,
                 size: Sizes = Sizes.MEDIUM,
                 speed: int = 30,
                 life_span: int = 100):
        if speed < 0:
            raise Exception("A Race cannot have a negative speed")

        if life_span < 0:
            raise Exception("A Race cannot have a negative life span")

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

    def __str__(self) -> str:
        """Print the Race as it would be seen in a race description."""

        output = f"{self._name} Traits\n"

        output += f"Creature Type: {self._creature_type.value}\n"

        output += f"Size: {self._size.value}\n"

        output += f"Speed: {self._speed} feet\n"

        output += f"Lifespan: {self._life_span} years on average\n"

        output += f"As a{'n' if self._name[0].upper() in ['A', 'E', 'I', 'O', 'I'] else ''} {self._name}, you have"\
                  "these special traits."

        for feat in self._features:
            output += f"\n{feat.summary()}"

        return output
