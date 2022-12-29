"""
Johnny. From the Baldur's Gate: Descent into Avernus campaign that I am running with my friends.
"""

from rules import abilities, character, bonuses, magicitem
from rules.enums import AbilityNames, Alignments, Languages, ProficiencyLevels, Skills, Tools


def create(content: dict[str, dict[str, any]]) -> character.Character:
    """
    A method that creates and returns a character. For now this is the method of saving character configurations
    :param content: The compiled content of the source files
    :type content: dict[str, dict[str, any]]
    :return: The created character.
    :rtype: character.Character
    """

    custom_background = content["Backgrounds"]["Custom"](
        name="Underdark Experiment",
        background_abilities=abilities.Abilities(
            wisdom=2,
            constitution=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.DECEPTION: ProficiencyLevels.PROFICIENT,
                Skills.INSIGHT: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.POISONERS_KIT: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.UNDERCOMMON],
        ),
        feat=content["Feats"]["Lucky"](),
        personality_traits="I lie about almost everything, even when there's no good reason to.\n"
                           "Sarcasm and insults are my weapons of choice.",
        ideals="Independence. I am a free spirit – no one tells me what to do. (Chaotic)",
        bonds="I swindled and ruined a person who didn't deserve it. I seek to atone for my misdeeds but might never "
              "be able to forgive myself.",
        flaws="I'm too greedy for my own good. I can't resist taking a risk if there's money involved.")

    johnny = character.Character(
        name="Johnny",
        character_class=content["Classes"]["Moon Druid"](skill1=Skills.ARCANA,
                                                         skill2=Skills.SURVIVAL),
        character_species=content["Species"]["Drow"](
            content, ability=AbilityNames.WISDOM),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 11,
            AbilityNames.DEXTERITY: 15,
            AbilityNames.CONSTITUTION: 15,
            AbilityNames.INTELLIGENCE: 9,
            AbilityNames.WISDOM: 15,
            AbilityNames.CHARISMA: 15,
        },
        alignment=Alignments.CHAOTIC_NEUTRAL,
        player_name="Kelsey",
        language=Languages.ELVISH,
        age="101",
        height="4'11\"",
        weight="200 lb.",
        eyes="Purple",
        skin="Charcoal",
        hair="Black",
        appearance_image="characters/images/johnny.pdf",
    )

    johnny.level_up(0, hit_roll=3, content=content)
    johnny.level_up(0, hit_roll=3)
    johnny.level_up(0, hit_roll=3, feat=content["Feats"]["Dungeon Delver"]())
    johnny.level_up(0, hit_roll=2)
    johnny.level_up(0, hit_roll=6)

    johnny.set_armor(content["Armors"]["Studded Leather"]())
    johnny.set_shield(content["Armors"]["Shield"]())
    johnny.set_weapons([
        content["Weapons"]["Scimitar"](silvered=True),
        content["Weapons"]["Longsword"](
            name="Moon-Touched Longsword", magical=True),
    ])
    johnny.set_magic_items(magic_items=[  # TODO better magic items
        magicitem.MagicItem(name="Cloak of Billowing",
                            description="While wearing this cloak, you can use a bonus action to make it billow "
                                        "dramatically."),
        magicitem.MagicItem(name="Moon-Touched Sword",
                            description="In darkness, the unsheathed blade of this sword sheds moonlight, creating "
                                        "bright light in a 15-foot radius and dim light for an additional 15 feet.")
    ])

    return johnny
