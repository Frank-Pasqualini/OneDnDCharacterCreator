"""
Zylith. From the Baldur's Gate: Descent into Avernus campaign that I am running with my friends.
"""

from rules import abilities, character, bonuses
from rules.enums import AbilityNames, Alignments, Languages, ProficiencyLevels, Skills, SpellLists, Tools


def create(content: dict[str, dict[str, any]]) -> character.Character:
    """
    A method that creates and returns a character. For now this is the method of saving character configurations
    :param content: The compiled content of the source files
    :type content: dict[str, dict[str, any]]
    :return: The created character.
    :rtype: character.Character
    """

    custom_background = content["Backgrounds"]["Custom"](
        name="Hunter",
        background_abilities=abilities.Abilities(
            dexterity=2,
            wisdom=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.PERCEPTION: ProficiencyLevels.PROFICIENT,
                Skills.STEALTH: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.NAVIGATORS_TOOLS: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.ELVISH],
        ),
        feat=content["Feats"]["Magic Initiate"](spell_list=SpellLists.PRIMAL,
                                                ability=AbilityNames.WISDOM,
                                                cantrip1=content["Spells"]["Guidance"](
                                                ),
                                                cantrip2=content["Spells"]["Spare the Dying"](
                                                ),
                                                spell=content["Spells"]["Ensnaring Strike"]()),
        personality_traits="Flattery is my preferred trick for getting what I want.\n"
                           "I fall in and out of love easily, and am always pursuing someone.",
        ideals="Creativity. I never run the same con twice.",
        bonds="I owe everything to my mentor—a horrible person who's probably rotting in jail somewhere.",
        flaws="I'm convinced that no one could ever fool me the way I fool others.")

    syd = character.Character(
        name="Sybrilla Liadon",
        character_class=content["Classes"]["Hunter Ranger"](content=content,
                                                            skill1=Skills.ANIMAL_HANDLING,
                                                            skill2=Skills.INSIGHT,
                                                            skill3=Skills.INVESTIGATION,
                                                            expertise1=Skills.INVESTIGATION,
                                                            expertise2=Skills.PERCEPTION),
        race=content["Races"]["Wood Elf"](
            content, ability=AbilityNames.WISDOM).half_race("Half-Elf", 80),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 9,
            AbilityNames.DEXTERITY: 14,
            AbilityNames.CONSTITUTION: 12,
            AbilityNames.INTELLIGENCE: 10,
            AbilityNames.WISDOM: 15,
            AbilityNames.CHARISMA: 12,
        },
        alignment=Alignments.CHAOTIC_GOOD,
        player_name="Rachel",
        language=Languages.SYLVAN,
        age="26",
        height="6'0\"",
        weight="172 lb.",
        eyes="Hazel",
        skin="Sun-Kissed",
        hair="Brown/Shaved Sides Bun",
        faction="Elturel",
        appearance_image="characters/images/syd.pdf",
        faction_image="characters/images/elturel.pdf",
    )

    syd.level_up(
        0, hit_roll=6, fighting_style=content["Feats"]["Fighting Style: Archery"]())
    syd.level_up(0, hit_roll=5)
    syd.level_up(0, hit_roll=5, feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.WISDOM,
                                                                                   ability2=AbilityNames.WISDOM))
    syd.level_up(0, hit_roll=5, content=content)

    syd.set_armor(content["Armors"]["Breastplate"]())
    syd.set_shield(content["Armors"]["Shield"]())
    syd.set_weapons([
        content["Weapons"]["Longbow"](),
        content["Weapons"]["Shortsword"](name="Silvered Shortsword"),
        content["Weapons"]["Dagger"](name="Silvered Dagger"),
    ])

    return syd
