"""
A spell that a character can cast.
"""

from abc import ABC

from rules.common import ordinal, validate_string
from rules.enums import SpellLists, SpellSchools


class Spell(ABC):
    """
    A spell that a character can cast.
    """

    _name: str
    _spell_lists: list[SpellLists]
    _level: int
    _school: SpellSchools
    _ritual: bool
    _casting_time: str
    _spell_range: str
    _verbal_components: bool
    _somatic_components: bool
    _material_components: bool
    _material_components_list: str | None
    _concentration: bool
    _duration: str
    _description: str
    _at_higher_levels: str

    def __init__(self,
                 name: str,
                 spell_lists: list[SpellLists],
                 level: int,
                 school: SpellSchools,
                 spell_range: str,
                 description: str,
                 ritual: bool = False,
                 casting_time: str = "1 action",
                 verbal_components: bool = False,
                 somatic_components: bool = False,
                 material_components: bool = False,
                 material_components_list: str = None,
                 concentration: bool = False,
                 duration: str = "Instantaneous",
                 at_higher_levels: str = None,
                 ):
        if level < 0 or level > 9:
            raise Exception("Invalid spell level")

        if material_components_list is not None:
            for component in material_components_list:
                validate_string(component)

        if (material_components_list is not None) != material_components:
            raise Exception(
                "If and only if a spell has material components they should be listed")

        self._name = validate_string(name)
        self._spell_lists = spell_lists
        self._level = level
        self._school = school
        self._ritual = ritual
        self._casting_time = validate_string(casting_time)
        self._spell_range = validate_string(spell_range)
        self._verbal_components = verbal_components
        self._somatic_components = somatic_components
        self._material_components = material_components
        self._material_components_list = material_components_list
        self._concentration = concentration
        self._duration = validate_string(duration)
        self._description = validate_string(description)
        self._at_higher_levels = at_higher_levels

    def get_school(self) -> SpellSchools:
        return self._school

    def get_spell_lists(self) -> list[SpellLists]:
        return self._spell_lists

    def get_level(self) -> int:
        return self._level

    def get_name(self) -> str:
        return self._name

    def summary(self) -> str:
        return self._name + (" (C)" if self._concentration else "") + (" (R)" if self._ritual else "")

    def __str__(self) -> str:
        output = f"{self._name}\n"

        output += f"{ordinal(self._level)}-Level {self._school.value} Spell"
        output += f" ({', '.join([str(spell_list.value) for spell_list in self._spell_lists])})"
        output += f"{' (ritual)' if self._ritual else ''}\n"

        output += f"Casting Time: {self._casting_time}\n"

        output += f"Range: {self._spell_range}\n"

        component_types = ["V" if self._verbal_components else None,
                           "S" if self._somatic_components else None,
                           "M" if self._material_components else None]
        component_types = [
            component_type for component_type in component_types if component_type is not None]
        output += f"Component: {', '.join(component_types)}"
        output += f"{' (' + self._material_components_list + ')' if self._material_components else ''}\n"

        output += f"Duration: {'Concentration, up to ' if self._concentration else ''}{self._duration}\n"

        output += f"{self._description}"

        if self._at_higher_levels is not None:
            output += f"\nAt Higher Levels. {self._at_higher_levels}"

        return output

    def __lt__(self, other) -> bool:
        return str(self._name) < str(other)

    def __gt__(self, other) -> bool:
        return str(self._name) > str(other)

    def __eq__(self, other):
        return self._name == other

    def __hash__(self) -> int:
        return hash(self._name)


def calculate_spell_name_width(spell: Spell) -> float:
    """
    Calculate the width of a string when printed in a non monospace font
    https://gist.github.com/aminnj/5ca372aa2def72fb017b531c894afdca
    :param spell: the string to find the width of
    :type spell: str
    :return: the width of the string
    :rtype: float
    """

    if spell is None:
        return 0

    size = 0.0

    widths = {
        " ": 4.4453125,
        "!": 4.4453125,
        '"': 5.6796875,
        "#": 8.8984375,
        "$": 8.8984375,
        "%": 14.2265625,
        "&": 10.671875,
        "'": 3.0546875,
        "(": 5.328125,
        ")": 5.328125,
        "*": 6.2265625,
        "+": 9.34375,
        ",": 4.4453125,
        "-": 5.328125,
        ".": 4.4453125,
        "/": 4.4453125,
        "0": 8.8984375,
        "1": 7.7228125,
        "2": 8.8984375,
        "3": 8.8984375,
        "4": 8.8984375,
        "5": 8.8984375,
        "6": 8.8984375,
        "7": 8.8984375,
        "8": 8.8984375,
        "9": 8.8984375,
        ":": 4.4453125,
        ";": 4.4453125,
        "<": 9.34375,
        "=": 9.34375,
        ">": 9.34375,
        "?": 8.8984375,
        "@": 16.2421875,
        "A": 10.671875,
        "B": 10.671875,
        "C": 11.5546875,
        "D": 11.5546875,
        "E": 10.671875,
        "F": 9.7734375,
        "G": 12.4453125,
        "H": 11.5546875,
        "I": 4.4453125,
        "J": 8,
        "K": 10.671875,
        "L": 8.8984375,
        "M": 13.328125,
        "N": 11.5546875,
        "O": 12.4453125,
        "P": 10.671875,
        "Q": 12.4453125,
        "R": 11.5546875,
        "S": 10.671875,
        "T": 9.7734375,
        "U": 11.5546875,
        "V": 10.671875,
        "W": 15.1015625,
        "X": 10.671875,
        "Y": 10.671875,
        "Z": 9.7734375,
        "[": 4.4453125,
        "\\": 4.4453125,
        "]": 4.4453125,
        "^": 7.5078125,
        "_": 8.8984375,
        "`": 5.328125,
        "a": 8.8984375,
        "b": 8.8984375,
        "c": 8,
        "d": 8.8984375,
        "e": 8.8984375,
        "f": 4.15921875,
        "g": 8.8984375,
        "h": 8.8984375,
        "i": 3.5546875,
        "j": 3.5546875,
        "k": 8,
        "l": 3.5546875,
        "m": 13.328125,
        "n": 8.8984375,
        "o": 8.8984375,
        "p": 8.8984375,
        "q": 8.8984375,
        "r": 5.328125,
        "s": 8,
        "t": 4.4453125,
        "u": 8.8984375,
        "v": 8,
        "w": 11.5546875,
        "x": 8,
        "y": 8,
        "z": 8,
        "{": 5.34375,
        "|": 4.15625,
        "}": 5.34375,
        "~": 9.34375,
    }

    for char in spell.summary():
        size += widths[char]

    return size
