"""
A set of things a character can be proficient in (plus extras).
"""

from __future__ import annotations

import logging

from rules.enums import AbilityNames, ArmorTraining, ArtisansTools, GamingSets, Languages, ProficiencyLevels
from rules.enums import MusicalInstruments, Skills, Tools, WeaponTypes


class Bonuses:
    """
    A set of things a character can be proficient in (plus extras).
    """

    _saving_throws: dict[AbilityNames, ProficiencyLevels]
    _skills: dict[Skills, ProficiencyLevels]
    _tools: dict[ArtisansTools | GamingSets |
                 MusicalInstruments | Tools, ProficiencyLevels]
    _armor_training: list[ArmorTraining]
    _weapon_types: list[WeaponTypes]
    _languages: list[Languages]
    _initiative: ProficiencyLevels
    _hp_bonus: int

    def __init__(self,
                 saving_throws: dict[AbilityNames, ProficiencyLevels] = None,
                 skills: dict[Skills, ProficiencyLevels] = None,
                 tools: dict[ArtisansTools | GamingSets |
                             MusicalInstruments | Tools, ProficiencyLevels] = None,
                 armor_training: list[ArmorTraining] = None,
                 weapon_types: list[WeaponTypes] = None,
                 languages: list[Languages] = None,
                 initiative: ProficiencyLevels = ProficiencyLevels.NONE,
                 hp_bonus: int = 0):

        self._saving_throws = saving_throws if saving_throws is not None else {}
        self._skills = skills if skills is not None else {}
        self._tools = tools if tools is not None else {}
        self._armor_training = armor_training if armor_training is not None else []
        self._weapon_types = weapon_types if weapon_types is not None else []
        self._languages = languages if languages is not None else []
        self._initiative = initiative
        self._hp_bonus = hp_bonus

    def get_saving_throws(self) -> dict[AbilityNames, ProficiencyLevels]:
        return self._saving_throws

    def get_skills(self) -> dict[Skills, ProficiencyLevels]:
        return self._skills

    def get_tools(self) -> dict[ArtisansTools | GamingSets | MusicalInstruments | Tools, ProficiencyLevels]:
        return self._tools

    def get_armor_training(self) -> list[ArmorTraining]:
        return self._armor_training

    def get_weapon_types(self) -> list[WeaponTypes]:
        return self._weapon_types

    def get_languages(self) -> list[Languages]:
        return self._languages

    def get_initiative(self) -> ProficiencyLevels:
        return self._initiative

    def get_hp_bonus(self) -> int:
        return self._hp_bonus

    def tools_summary(self) -> list[str]:
        """
        Gets a summary of all the tool proficiencies
        :return: A list of tools and their proficiency levels
        :rtype: list[str]
        """
        tools = ["*" + str(tool.value) if self._tools[tool] == ProficiencyLevels.EXPERT else
                 str(tool.value) for tool in sorted(self._tools.keys())]
        return tools

    def summary(self) -> str:
        """
        Gets a summary of all bonuses
        :return: A summary of all bonuses
        :rtype: str
        """
        output = f"Armor Training: {', '.join([str(armor.value) for armor in sorted(self._armor_training)])}\n\n"

        output += f"Weapons: {', '.join([str(armor.value) for armor in sorted(self._weapon_types)])}\n\n"

        output += f"Tools: {', '.join(self.tools_summary())}\n\n"

        output += f"Languages: {', '.join([str(language.value) for language in sorted(self._languages)])}"

        return output

    def __add__(self, other: Bonuses) -> Bonuses:
        saving_throws = {}
        for key in list(self._saving_throws.keys()) + list(other.get_saving_throws().keys()):
            saving_throws[key] = max(self._saving_throws.get(key, 0),
                                     other.get_saving_throws().get(key, 0))
            if self._saving_throws.get(key, 0) == other.get_saving_throws().get(key,
                                                                                0) and self._saving_throws.get(key,
                                                                                                               0) != 0:
                logging.warning("You have two or more instances of proficiency level %s for saving throw %s. Consider "
                                "changing one.", self._saving_throws[key].name, key.value)

        skills = {}
        for key in list(self._skills.keys()) + list(other.get_skills().keys()):
            skills[key] = max(self._skills.get(key, 0),
                              other.get_skills().get(key, 0))
            if self._skills.get(key, 0) == other.get_skills().get(key, 0) and self._skills.get(key, 0) != 0:
                logging.warning("You have two or more instances of proficiency level %s for skill %s. Consider "
                                "changing one.", self._skills[key].name, key.value)

        tools = {}
        for key in list(self._tools.keys()) + list(other.get_tools().keys()):
            tools[key] = max(self._tools.get(key, 0),
                             other.get_tools().get(key, 0))
            if self._tools.get(key, 0) == other.get_tools().get(key, 0) and self._tools.get(key, 0) != 0:
                logging.warning("You have two or more instances of proficiency level %s for tool %s. Consider "
                                "changing one.", self._tools[key].name, key.value)

        armor_training = list(set(self._armor_training) |
                              set(other.get_armor_training()))

        weapon_types = list(set(self._weapon_types) |
                            set(other.get_weapon_types()))

        languages = list(set(self._languages) | set(other.get_languages()))
        if len(list(set(self._languages) & set(other.get_languages()))) != 0:
            logging.warning(
                "Two or more bonuses give you the same languages. Consider changing one.")

        initiative = max(self._initiative, other.get_initiative())
        if self._initiative == other.get_initiative() and self._initiative != ProficiencyLevels.NONE:
            logging.warning("You have two or more instances of proficiency level %s for initiative. Consider changing "
                            "one.", self._initiative.name)

        hp_bonus = self._hp_bonus + other.get_hp_bonus()

        return Bonuses(saving_throws=saving_throws,
                       skills=skills,
                       tools=tools,
                       armor_training=armor_training,
                       weapon_types=weapon_types,
                       languages=languages,
                       initiative=initiative,
                       hp_bonus=hp_bonus)
