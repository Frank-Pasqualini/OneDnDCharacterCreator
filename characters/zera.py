"""
Fena. From the Baldur's Gate: Descent into Avernus campaign that I am running with my family.
"""

from rules import abilities, character, bonuses, magicitem
from rules.enums import AbilityNames, Alignments, ArtisansTools, Languages, ProficiencyLevels, Skills


def create(content: dict[str, dict[str, any]]) -> character.Character:
    """
    A method that creates and returns a character. For now this is the method of saving character configurations
    :param content: The compiled content of the source files
    :type content: dict[str, dict[str, any]]
    :return: The created character.
    :rtype: character.Character
    """

    custom_background = content["Backgrounds"]["Custom"](
        name="Shard of Zariel ",
        background_abilities=abilities.Abilities(
            strength=2,
            charisma=1,
        ),
        background_bonuses=bonuses.Bonuses(
            skills={
                Skills.INSIGHT: ProficiencyLevels.PROFICIENT,
                Skills.MEDICINE: ProficiencyLevels.PROFICIENT,
            },
            tools={
                ArtisansTools.ALCHEMISTS_SUPPLIES: ProficiencyLevels.PROFICIENT
            },
            languages=[Languages.CELESTIAL],
        ),
        feat=content["Feats"]["Savage Attacker"](),
        personality_traits="My praise and trust are earned and never given freely.\n"
                           "I like everything clean and organized.",
        ideals="Honor. The way I conduct myself determines my reward in the afterlife. (Lawful)",
        bonds="I must keep a written record of my beliefs and the sins that I witness. When finished, this book will "
              "be my gift to the multiverse.",
        flaws="I offer forgiveness too readily.")

    zera = character.Character(
        name="Zera",
        character_class=content["Classes"]["Watchers Paladin"](skill1=Skills.ATHLETICS,
                                                               skill2=Skills.INTIMIDATION),
        character_species=content["Species"]["Copper Dragonborn"](),
        background=custom_background,
        starting_abilities={
            AbilityNames.STRENGTH: 16,
            AbilityNames.DEXTERITY: 10,
            AbilityNames.CONSTITUTION: 16,
            AbilityNames.INTELLIGENCE: 12,
            AbilityNames.WISDOM: 13,
            AbilityNames.CHARISMA: 20,
        },
        alignment=Alignments.LAWFUL_GOOD,
        player_name="Mom",
        language=Languages.INFERNAL,
        age="30",
        height="6'9\"",
        weight="350 lb.",
        eyes="Turquoise",
        skin="Copper",
        hair="None",
        appearance_image="characters/images/zera.pdf",
    )

    zera.level_up(
        0, hit_roll=7, fighting_style=content["Feats"]["Fighting Style: Defense"]())
    zera.level_up(0, hit_roll=7, content=content)
    zera.level_up(0, hit_roll=7, feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.CHARISMA,
                                                                                    ability2=AbilityNames.CHARISMA))
    zera.level_up(0, hit_roll=7)
    zera.level_up(0, hit_roll=7)
    zera.level_up(0, hit_roll=7)
    zera.level_up(0, hit_roll=6, feat=content["Feats"]["Ability Score Improvement"](ability1=AbilityNames.CONSTITUTION,
                                                                                    ability2=AbilityNames.CONSTITUTION))
    zera.level_up(0, hit_roll=6)
    zera.level_up(0, hit_roll=6)
    zera.level_up(0, hit_roll=9)
    zera.level_up(0, hit_roll=1, feat=content["Feats"]["Ability Score Improvement"](
        ability1=AbilityNames.STRENGTH,
        ability2=AbilityNames.STRENGTH
    ))
    zera.level_up(0, hit_roll=5)

    zera.set_armor(content["Armors"]["Plate"]())
    zera.set_weapons([
        content["Weapons"]["Longsword"](
            name="Sword of Zariel", magical=True),
        content["Weapons"]["Longsword"](
            name="Dragon Slayer Longsword", attack_bonus=1, damage_bonus=1, magical=True),
    ])

    zera.set_magic_items([  # TODO better magic items
        magicitem.MagicItem(name="Sword of Zariel",
                            description="This longsword belonged to the angel Zariel before her fall from grace. "
                                        "Fashioned from celestial steel, it gives off a faint glow and hum. The "
                                        "weapon chooses who can attune to it and who can't. It desires a wielder who "
                                        "embodies bravery and heroism.\n"
                                        "Attunement. The sword allows you to attune to it immediately, without having "
                                        "to take a short rest. The first time you attune to the sword, "
                                        "you are transformed into a heavenly, idealized version of yourself, "
                                        "blessed with otherworldly beauty and a touch of heaven in your heart. "
                                        "Neither magic nor divine intervention can reverse this transformation. Your "
                                        "alignment becomes lawful good, and you gain the following traits:\n"
                                        "• Angelic Language. You can speak, read. and write Celestial.\n"
                                        "• Celestial Resistance. You have resistance to necrotic and radiant damage.\n"
                                        "• Divine Presence. Your Charisma score becomes 20, unless it is already 20 "
                                        "or higher.\n"
                                        "• Feathered Wings. You sprout a beautiful pair of feathered wings that grant "
                                        "you a flying speed of 90 feet and the ability to hover. If you already have "
                                        "a different kind of wings, these new wings replace the old ones, which fall "
                                        "off.\n"
                                        "• Truesight. Your eyes become luminous pools of silver. You can see in "
                                        "normal and magical darkness, see invisible creatures and objects, "
                                        "automatically detect visual illusions and succeed on saving throws against "
                                        "them, perceive the original form of a shapechanger or a creature that is "
                                        "transformed by magic, and see into the Ethereal Plane, all within a range of "
                                        "60 feet.\n"
                                        "• New Personality. You gain new personality traits. These traits override "
                                        "any conflicting personality trait, ideal, bond, or flaw.\n"
                                        "Holy Light. The sword sheds bright light in a 5-foot radius and dim light "
                                        "for an additional 5 feet. Fiends find the sword's light disconcerting and "
                                        "painful, even if they can't see it, and have disadvantage on attack rolls "
                                        "made within the weapon's radius of bright light.\n"
                                        "As a bonus action, you can intensify the sword's light, causing it to shed "
                                        "bright light in a 15-foot radius and dim light for an additional 15 feet, "
                                        "or reduce its glow to its normal intensity.\n"
                                        "Angelic Resolve. When attuned to the sword you can't be charmed or "
                                        "frightened.\n"
                                        "Angelic Defense. When attuned the sword you gain a +1 bonus to Armor Class.\n"
                                        "Searing Radiance. The sword deals an extra 9 (2d8) radiant damage to any "
                                        "creature it hits, or 16 (3d10) radiant damage if you're wielding the weapon "
                                        "with two hands. An evil creature that takes this radiant damage must succeed "
                                        "on a DC 17 Constitution saving throw or be blinded until the end of its next "
                                        "turn.\n"
                                        "Sentience. The Sword of Zariel is a sentient, lawful good item with an "
                                        "Intelligence of 10, a Wisdom of 20, and a Charisma of 18. It has hearing and "
                                        "normal vision out to a range of 30 feet.\n"
                                        "The sword communicates by transmitting emotion to the creature carrying or "
                                        "wielding it.\n"
                                        "Truth Seer. While holding the sword, you gain advantage on all Wisdom ("
                                        "Insight) checks."),
        magicitem.MagicItem(name="Dragon Slayer Sword",
                            description="You gain a +1 bonus to attack and damage rolls made with this magic weapon.\n"
                                        "When you hit a dragon with this weapon, the dragon takes an extra 3d6 damage. "
                                        "For the purpose of this weapon, \"dragon\" refers to any creature with the "
                                        "dragon type, including dragon turtles and wyverns.")
    ])

    return zera
