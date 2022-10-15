"""
Zylith. From the Baldur's Gate: Descent into Avernus campaign that I am running with my friends.
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
        name="Detective",
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
                Tools.FORGERY_KIT: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.INFERNAL],
        ),
        feat=content["Feats"]["Lucky"](),
        description="To you, this is just a way to earn a living. You go to work, do what needs to be done, "
                    "and get paid. Anyone who pursues crime for thrill-seeking, to strike back at unjust authorities, "
                    "or anything else are amateurs, and they're liable to get you arrested or killed with their "
                    "idiocy.\n"
                    "You know who your parents are.\n"
                    "Both parents were humans, their infernal heritage dormant until you came along.\n"
                    "Born in home of a family friend.\n"
                    "3 Siblings, 1 younger, 1 twin, 1 older.\n"
                    "Raised by Grandparents. One parent abandoned you and one disappeared to an unknown fate.\n"
                    "Modest lifestyle but moved around a lot, with a few close friends.\n"
                    "I resented authority in my younger days and saw a life of crime as the best way to fight against "
                    "tyranny and oppression.\n"
                    "I decided to turn my natural lucky streak into the basis of a career, though I still realize "
                    "that improving my skills is essential.\n"
                    "Worked 2 jobs.\n"
                    "Lost sentimental dragon scale oin an adventure.\n"
                    "Went on an adventure and was poisoned by a monster, but recovered.",
        personality_traits="The first thing I do in a new place is note the locations of everything valuable—or where "
                           "such things could be hidden.\n"
                           "The best way to get me to do something is to tell me I can't do it.",
        ideals="Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)",
        bonds="I'm trying to pay off an old debt I owe to a generous benefactor.",
        flaws="I turn tail and run when things look bad.\n"
              "Guilty Pleasure: A smile from a pretty face.")

    zylith = character.Character(
        name="Zylith",
        character_class=content["Classes"]["Inquisitive Rogue"](skill1=Skills.DECEPTION,
                                                                skill2=Skills.INSIGHT,
                                                                skill3=Skills.INVESTIGATION,
                                                                skill4=Skills.PERSUASION,
                                                                expertise1=Skills.INSIGHT,
                                                                expertise2=Skills.SLEIGHT_OF_HAND,
                                                                language=Languages.COMMON_SIGN_LANGUAGE),
        race=content["Races"]["Chthonic Tiefling"](
            content, ability=AbilityNames.CHARISMA),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 7,
            AbilityNames.DEXTERITY: 16,
            AbilityNames.CONSTITUTION: 10,
            AbilityNames.INTELLIGENCE: 13,
            AbilityNames.WISDOM: 12,
            AbilityNames.CHARISMA: 13,
        },
        alignment=Alignments.CHAOTIC_GOOD,
        player_name="Mira",
        language=Languages.ABYSSAL,
        age="31",
        height="6'1\"",
        weight="150 lb.",
        eyes="Purple",
        skin="Light Blue",
        hair="White",
        faction="Baldur's Gate",
        appearance_image="characters/images/zylith.pdf",
        faction_image="characters/images/baldurs_gate.pdf",
        allies="A magistrate once kept you out of jail in return for information on a powerful crime lord."
    )

    zylith.level_up(0, hit_roll=5)
    zylith.level_up(0, hit_roll=5)
    zylith.level_up(0, hit_roll=5, feat=content["Feats"]["Telepathic"](
        content, ability=AbilityNames.CHARISMA))
    zylith.level_up(0, hit_roll=5)

    zylith.set_armor(content["Armors"]["Studded Leather"]())
    zylith.set_weapons([
        content["Weapons"]["Rapier"](),
        content["Weapons"]["Hand Crossbow"](name="Hand Crossbow"),
        content["Weapons"]["Dagger"](name="Silvered Dagger"),
    ])
    zylith.set_magic_items(magic_items=[
        magicitem.MagicItem(name="Gloves of Thievery",
                            description="These gloves are invisible while worn. While wearing them, you gain a +5 "
                                        "bonus to Dexterity (Sleight of Hand) checks and Dexterity checks made to "
                                        "pick locks.")
    ])

    return zylith
