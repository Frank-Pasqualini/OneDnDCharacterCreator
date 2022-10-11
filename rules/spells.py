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

    def get_spell_lists(self) -> list[SpellLists]:
        return self._spell_lists

    def get_level(self) -> int:
        return self._level

    def get_name(self) -> str:
        return self._name

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
        return self._name < other

    def __gt__(self, other) -> bool:
        return self._name > other

    def __hash__(self) -> int:
        return hash(self._name)
