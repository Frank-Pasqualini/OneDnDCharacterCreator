from __future__ import annotations

from rules.Enums import AbilityNames, ArtisansTools, GamingSets, ProficiencyLevels, MusicalInstruments, Skills, Tools


class Bonuses:
    """A set of things a character can be proficient in (plus extras)."""

    _saving_throws: dict[AbilityNames, ProficiencyLevels]
    _skills: dict[Skills, ProficiencyLevels]
    _artisans_tools: dict[ArtisansTools, ProficiencyLevels]
    _gaming_sets: dict[GamingSets, ProficiencyLevels]
    _musical_instruments: dict[MusicalInstruments, ProficiencyLevels]
    _tools: dict[Tools, ProficiencyLevels]
    _initiative: ProficiencyLevels
    _hp_bonus: int

    def __init__(self,
                 saving_throws: dict[AbilityNames, ProficiencyLevels] = None,
                 skills: dict[Skills, ProficiencyLevels] = None,
                 artisans_tools: dict[ArtisansTools, ProficiencyLevels] = None,
                 gaming_sets: dict[GamingSets, ProficiencyLevels] = None,
                 musical_instruments: dict[MusicalInstruments, ProficiencyLevels] = None,
                 tools: dict[Tools, ProficiencyLevels] = None,
                 initiative: ProficiencyLevels = ProficiencyLevels.NONE,
                 hp_bonus: int = 0):

        self._saving_throws = saving_throws if saving_throws is not None else {}
        self._skills = skills if skills is not None else {}
        self._artisans_tools = artisans_tools if artisans_tools is not None else {}
        self._gaming_sets = gaming_sets if gaming_sets is not None else {}
        self._musical_instruments = musical_instruments if musical_instruments is not None else {}
        self._tools = tools if tools is not None else {}
        self._initiative = initiative
        self._hp_bonus = hp_bonus

    def get_saving_throws(self) -> dict[AbilityNames, ProficiencyLevels]:
        return self._saving_throws

    def get_skills(self) -> dict[Skills, ProficiencyLevels]:
        return self._skills

    def get_artisans_tools(self) -> dict[ArtisansTools, ProficiencyLevels]:
        return self._artisans_tools

    def get_gaming_sets(self) -> dict[GamingSets, ProficiencyLevels]:
        return self._gaming_sets

    def get_musical_instruments(self) -> dict[MusicalInstruments, ProficiencyLevels]:
        return self._musical_instruments

    def get_tools(self) -> dict[Tools, ProficiencyLevels]:
        return self._tools

    def get_initiative(self) -> ProficiencyLevels:
        return self._initiative

    def get_hp_bonus(self) -> int:
        return self._hp_bonus

    def __add__(self, other: Bonuses) -> Bonuses:
        """Take the highest of the two values."""

        saving_throws = {}
        for key in list(self._saving_throws.keys()) + list(other.get_saving_throws().keys()):
            saving_throws[key] = max(self._saving_throws.get(key, 0),
                                     other.get_saving_throws().get(key, 0))

        skills = {}
        for key in list(self._skills.keys()) + list(other.get_skills().keys()):
            skills[key] = max(self._skills.get(key, 0),
                              other.get_skills().get(key, 0))

        artisans_tools = {}
        for key in list(self._artisans_tools.keys()) + list(other.get_artisans_tools().keys()):
            artisans_tools[key] = max(self._artisans_tools.get(key, 0),
                                      other.get_artisans_tools().get(key, 0))

        gaming_sets = {}
        for key in list(self._gaming_sets.keys()) + list(other.get_gaming_sets().keys()):
            gaming_sets[key] = max(self._gaming_sets.get(key, 0),
                                   other.get_gaming_sets().get(key, 0))

        musical_instruments = {}
        for key in list(self._musical_instruments.keys()) + list(other.get_musical_instruments().keys()):
            musical_instruments[key] = max(self._musical_instruments.get(key, 0),
                                           other.get_musical_instruments().get(key, 0))

        tools = {}
        for key in list(self._tools.keys()) + list(other.get_tools().keys()):
            tools[key] = max(self._tools.get(key, 0),
                             other.get_tools().get(key, 0))
            
        initiative = max(self._initiative, other.get_initiative())
        hp_bonus = self._hp_bonus + other.get_hp_bonus()

        return Bonuses(saving_throws=saving_throws,
                       skills=skills,
                       artisans_tools=artisans_tools,
                       gaming_sets=gaming_sets,
                       musical_instruments=musical_instruments,
                       tools=tools,
                       initiative=initiative,
                       hp_bonus=hp_bonus)
