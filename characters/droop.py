"""
Droop. From the Baldur's Gate: Descent into Avernus campaign that I am running with my family.
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
        name="Faithful of Lathander",
        background_abilities=abilities.Abilities(
            intelligence=1,
            wisdom=1,
            charisma=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.MEDICINE: ProficiencyLevels.PROFICIENT,
                Skills.RELIGION: ProficiencyLevels.PROFICIENT,
            },
            tools={
                Tools.HERBALISM_KIT: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.CELESTIAL],
        ),
        feat=content["Feats"]["Healer"](),
        description="You devoted yourself to service in a temple, either nestled in a town or secluded in a sacred "
                    "grove. There you performed hallowed rites in honor of a god or pantheon. You served under a "
                    "priest and studied religion. Thanks to your priest's instruction and your own devotion, "
                    "you also learned how to channel divine power in service to your place of worship and the people "
                    "who prayed there.",
        personality_traits="Nothing can shake my optimistic attitude.\n"
                           "I am tolerant of other faiths and respect the worship of other gods.",
        ideals="Charity. I always try to help those in need, no matter what the personal cost. (Good)",
        bonds="Everything I do is for the Common people.",
        flaws="Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.")

    droop = character.Character(
        name="Droop",
        character_class=content["Classes"]["Life Cleric"](skill1=Skills.HISTORY,
                                                          skill2=Skills.INSIGHT),
        character_species=content["Species"]["Goblin"](),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 8,
            AbilityNames.DEXTERITY: 12,
            AbilityNames.CONSTITUTION: 12,
            AbilityNames.INTELLIGENCE: 13,
            AbilityNames.WISDOM: 15,
            AbilityNames.CHARISMA: 13,
        },
        alignment=Alignments.LAWFUL_GOOD,
        player_name="Hanna",
        language=Languages.GOBLIN,
        age="10",
        height="3'7\"",
        weight="37 lb.",
        eyes="Yellow",
        skin="Green",
        hair="Brown",
        faction="Church of Lathander",
        appearance_image="characters/images/droop.pdf",
        faction_image="characters/images/lathander.pdf",
    )

    droop.level_up(
        0, holy_order=content["Holy Orders"]["Holy Order: Protector"]())
    droop.level_up(0, content=content)
    droop.level_up(0, feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.WISDOM,
                                                                         ability2=AbilityNames.WISDOM))
    droop.level_up(0)
    droop.level_up(0)
    droop.level_up(0)
    droop.level_up(0, feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.WISDOM,
                                                                         ability2=AbilityNames.WISDOM))
    droop.level_up(
        0, holy_order=content["Holy Orders"]["Holy Order: Thaumaturge"]())
    droop.level_up(0)
    droop.level_up(0)
    droop.level_up(0, feat=content["Feats"]["Inspiring Leader"](
        ability=AbilityNames.CHARISMA))
    droop.level_up(0)

    droop.set_armor(content["Armors"]["Scale Mail"]())
    droop.set_shield(content["Armors"]["Shield"]())
    droop.set_weapons([
        content["Weapons"]["Mace"](
            name="Hellfire Mace", magical=True),
    ])

    droop.set_magic_items([  # TODO better magic items
        magicitem.MagicItem(name="Hellfire Weapon",
                            description="This weapon is fashioned from infernal iron and traced with veins of "
                                        "hellfire that shed dim light in a 5-foot-radius.\n"
                                        "Any humanoid killed by an attack made with this weapon has its soul "
                                        "funneled into the River Styx, where it's reborn instantly as a lemure "
                                        "devil."),
        magicitem.MagicItem(name="Sanctuary Shard",
                            description="This item looks like a shard of frosted glass, about 7 inches in length. "
                                        "When handled, its inside shimmers with a faint blue light. A creature that "
                                        "uses its bonus action to break the shard can imbue its own hands with magic "
                                        "and cast one of the following spells immediately with its action:\n"
                                        "- At 1st level: detect magic, detect evil and good, or detect poison and "
                                        "disease.\n"
                                        "- At 2nd level: cure wounds or inflict wounds.\n"
                                        "If the creature does not use the spell until the beginning of its next turn "
                                        "the magic fizzles and the spell is lost.\n"
                                        "The shard can also be used as a material component to the revivify spell, "
                                        "in which case it is considered as a diamond worth 300gp. Moreover, "
                                        "this shard can be used to fuel a lamp of the departed. In all of the "
                                        "aforementioned uses the shard is consumed."),
    ])

    return droop
