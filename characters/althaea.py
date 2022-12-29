"""
Althaea Holimion. From the Baldur's Gate: Descent into Avernus campaign that I am running with my friends.
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
        name="Criminal",
        background_abilities=abilities.Abilities(
            wisdom=2,
            constitution=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.DECEPTION: ProficiencyLevels.PROFICIENT,
                Skills.STEALTH: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.THIEVES_TOOLS: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.ABYSSAL],
        ),
        feat=content["Feats"]["Savage Attacker"](),
        personality_traits="The first thing I do in a new place is note the locations of everything valuable-or where "
                           "such things could be hidden.\n"
                           "The best way to get me to do something is to tell me I can't do it.",
        ideals="Charity. I steal from the wealthy so that I can help people in need. (Good)",
        bonds="I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        flaws="I turn tail and run when things look bad.")

    althaea = character.Character(
        name="Althaea Holimion",
        character_class=content["Classes"]["Spores Druid"](skill1=Skills.ARCANA,
                                                           skill2=Skills.NATURE),
        character_species=content["Species"]["High Elf"](
            content, ability=AbilityNames.WISDOM),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 13,
            AbilityNames.DEXTERITY: 11,
            AbilityNames.CONSTITUTION: 14,
            AbilityNames.INTELLIGENCE: 14,
            AbilityNames.WISDOM: 13,
            AbilityNames.CHARISMA: 14,
        },
        alignment=Alignments.CHAOTIC_GOOD,
        player_name="Cassie",
        language=Languages.ELVISH,
        age="101",
        height="5'3\"",
        weight="135 lb.",
        eyes="Black",
        skin="Bronze",
        hair="Golden",
        appearance_image="characters/images/althaea.pdf",
    )

    althaea.level_up(0, hit_roll=5, content=content)
    althaea.level_up(0, hit_roll=5)
    althaea.level_up(0, hit_roll=5, feat=content["Feats"]["Tough"]())
    althaea.level_up(0, hit_roll=5)
    althaea.level_up(0, hit_roll=2)

    althaea.set_armor(content["Armors"]["Studded Leather"]())
    althaea.set_shield(content["Armors"]["Shield"]())
    althaea.set_weapons([
        content["Weapons"]["Quarterstaff"](),
    ])
    althaea.set_magic_items(magic_items=[  # TODO better magic items
        magicitem.MagicItem(name="Wand of Pyrotechnics",
                            description="This wand has 7 charges. While holding it, you can use an action to expend 1 "
                                        "of its charges and create a harmless burst of multicolored light at a point "
                                        "you can see up to 60 feet away. The burst of light is accompanied by a "
                                        "crackling noise that can be heard up to 300 feet away. The light is as "
                                        "bright as a torch flame but lasts only a second.\n"
                                        "The wand regains 1d6 + 1 expended charges daily at dawn. If you expend the "
                                        "wand's last charge, roll a d20. On a 1, the wand erupts in a harmless "
                                        "pyrotechnic display and is destroyed."),
    ])

    return althaea
