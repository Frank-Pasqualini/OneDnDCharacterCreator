"""
Nightshade Longseek. From the Baldur's Gate: Descent into Avernus campaign that I am running with my family.
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
            dexterity=2,
            intelligence=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.SLEIGHT_OF_HAND: ProficiencyLevels.PROFICIENT,
                Skills.STEALTH: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.POISONERS_KIT: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.DWARVISH],
        ),
        feat=content["Feats"]["Alert"](),
        description="You learned to earn your coin in dark alleyways, cutting purses or burgling shops. Perhaps you "
                    "were part of a small gang of like-minded wrongdoers, who looked out for each other. Or maybe you "
                    "were a lone wolf, fending for yourself against the local thieves' guild and older, more fearsome "
                    "lawbreakers.",
        personality_traits="The first thing I do in a new place is note the locations of everything valuable—or where "
                           "such things could be hidden.\n"
                           "The best way to get me to do something is to tell me I can't do it.",
        ideals="Redemption. There's a spark of good in everyone. (Good)",
        bonds="I will become the greatest thief that ever lived.",
        flaws="When I see something valuable, I can't think about anything but how to steal it.")

    nightshade = character.Character(
        name="Nightshade Longseek",
        character_class=content["Classes"]["Thief Rogue"](skill1=Skills.ATHLETICS,
                                                          skill2=Skills.DECEPTION,
                                                          skill3=Skills.INVESTIGATION,
                                                          skill4=Skills.PERSUASION,
                                                          expertise1=Skills.INVESTIGATION,
                                                          expertise2=Skills.SLEIGHT_OF_HAND,
                                                          language=Languages.COMMON_SIGN_LANGUAGE),
        race=content["Races"]["Human"](skill=Skills.HISTORY,
                                       versatile=content["Feats"]["Lucky"]()),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 11,
            AbilityNames.DEXTERITY: 16,
            AbilityNames.CONSTITUTION: 13,
            AbilityNames.INTELLIGENCE: 14,
            AbilityNames.WISDOM: 13,
            AbilityNames.CHARISMA: 15,
        },
        alignment=Alignments.CHAOTIC_GOOD,
        player_name="Brody",
        language=Languages.GOBLIN,
        age="27",
        height="5'2\"",
        weight="117 lb.",
        eyes="Blue",
        skin="Pale",
        hair="Blonde",
        faction="Elturel",
        appearance_image="characters/images/nightshade.pdf",
        faction_image="characters/images/elturel.pdf",
    )

    nightshade.level_up(0, hit_roll=6)
    nightshade.level_up(0, hit_roll=6)
    nightshade.level_up(0, hit_roll=6,
                        feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.DEXTERITY,
                                                                           ability2=AbilityNames.DEXTERITY))
    nightshade.level_up(0, hit_roll=6)
    nightshade.level_up(0, hit_roll=6)
    nightshade.level_up(
        0, hit_roll=5, expertise1=Skills.STEALTH, expertise2=Skills.DECEPTION)
    nightshade.level_up(0, hit_roll=5,
                        feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.CONSTITUTION,
                                                                           ability2=AbilityNames.INTELLIGENCE))
    nightshade.level_up(0, hit_roll=5)

    nightshade.set_armor(content["Armors"]["Studded Leather"]())
    nightshade.set_weapons([
        content["Weapons"]["Rapier"](name="Hellfire Rapier", magical=True),
        content["Weapons"]["Dagger"](name="Hellfire Dagger", magical=True),
    ])
    nightshade.set_magic_items([  # TODO better magic items
        magicitem.MagicItem(name="Hellfire Weapon",
                            description="This weapon is fashioned from infernal iron and traced with veins of "
                                        "hellfire that shed dim light in a 5-foot-radius.\n"
                                        "Any humanoid killed by an attack made with this weapon has its soul "
                                        "funneled into the River Styx, where it's reborn instantly as a lemure "
                                        "devil."),
        magicitem.MagicItem(name="Cloak of Elvenkind",
                            description="While you wear this cloak with its hood up, Wisdom (Perception) checks "
                                        "made to see you have disadvantage. and you have advantage on Dexterity ("
                                        "Stealth) checks made to hide, as the cloak's color shifts to camouflage "
                                        "you. Pulling the hood up or down requires an Action.")
    ])

    return nightshade
