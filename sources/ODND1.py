from rules import Backgrounds, Feats, Bonuses, Races, Spells
from rules.Enums import AbilityNames, ArtisansTools, DamageTypes, Languages, MusicalInstruments, ProficiencyLevels, \
    Sizes, Skills, SpellLists


class Alert(Feats.Feat):
    def __init__(self):
        super().__init__(name="Alert",
                         level=1,
                         description="Always on the lookout for danger, you gain the following benefits:\n"
                                     "Initiative Proficiency. When you roll Initiative, you can add your Proficiency "
                                     "Bonus to the roll.\n"
                                     "Initiative Swap. Immediately after you roll Initiative, you can swap your "
                                     "Initiative with the Initiative of one willing ally in the same combat. You "
                                     "can’t make this swap if you or the ally is Incapacitated.",
                         bonuses=Bonuses.Bonuses(initiative=ProficiencyLevels.PROFICIENT))


class Crafter(Feats.Feat):
    def __init__(self, tool1: ArtisansTools, tool2: ArtisansTools, tool3: ArtisansTools):
        if tool1 == tool2 or tool1 == tool3 or tool2 == tool3:
            raise Exception("All 3 tools should be unique")

        super().__init__(name="Crafter",
                         level=1,
                         description="You are adept at crafting things and bargaining with merchants, granting you "
                                     "the following benefits:\n"
                                     f"Tool Proficiency. You gain Tool Proficiency with {tool1.value}, {tool2.value}, "
                                     f"and {tool3.value}.\n"
                                     "Discount. Whenever you buy a nonmagical item, you receive a 20 percent discount "
                                     "on it.\n"
                                     "Faster Crafting. When you craft an item using a tool with which you have Tool "
                                     "Proficiency, the required crafting time is reduced by 20 percent.",
                         bonuses=Bonuses.Bonuses(artisans_tools={
                             tool1: ProficiencyLevels.PROFICIENT,
                             tool2: ProficiencyLevels.PROFICIENT,
                             tool3: ProficiencyLevels.PROFICIENT,
                         }))


class Healer(Feats.Feat):
    def __init__(self):
        super().__init__(name="Healer",
                         level=1,
                         description="You have the training and intuition to administer first aid and other care "
                                     "effectively, granting you the following benefits:\n"
                                     "Battle Medic. If you have a Healer’s Kit, you can expend one use of it and tend "
                                     "to a creature within 5 feet of you as an Action. That creature can expend one "
                                     "of its Hit Dice, and you then roll that die. The creature regains a number of "
                                     "Hit Points equal to the roll plus your Proficiency Bonus.\n"
                                     "Healing Rerolls. Whenever you roll a die to determine the number of Hit Points "
                                     "you restore with a spell or with this feat’s Battle Medic benefit, you can "
                                     "reroll the die if it rolls a 1, and you must use the new roll.")


class Lucky(Feats.Feat):
    def __init__(self):
        super().__init__(name="Lucky",
                         level=1,
                         description="You have inexplicable luck that can kick in at just the right moment, granting "
                                     "you the following benefits:\n"
                                     "Luck Points. You have a number of Luck Points equal to your Proficiency Bonus. "
                                     "You can spend the points on the benefits below, and you regain your expended "
                                     "Luck Points when you finish a Long Rest.\n"
                                     "Advantage. Immediately after you roll a d20 for a d20 Test, you can spend 1 "
                                     "Luck Point to give yourself Advantage on the roll.\n"
                                     "Disadvantage. When a creature rolls a d20 for an attack roll against you, "
                                     "you can spend 1 Luck Point to impose Disadvantage on that roll.")


class MagicInitiate(Feats.Feat):
    def __init__(self,
                 spell_list: SpellLists,
                 cantrip1: Spells.Spell,
                 cantrip2: Spells.Spell,
                 spell: Spells.Spell,
                 ability: AbilityNames):

        if cantrip1.get_level() != 0 or cantrip2.get_level() != 0 or spell.get_level() != 1:
            raise Exception("Invalid spell levels")

        if spell_list not in cantrip1.get_spell_lists() or spell_list not in cantrip2.get_spell_lists() or \
                spell_list not in spell.get_spell_lists():
            raise Exception("All spells must be in the proper Spell List")

        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception("Spellcasting ability must be one of the mental abilities.")

        super().__init__(name="Magic Initiate",
                         level=1,
                         description=f"You have learned the basics of a the {spell_list.value} magical tradition. You "
                                     "gain the following benefits related to that choice:\n"
                                     f"Two Cantrips. You learn {cantrip1.get_name()} and {cantrip2.get_name()}.\n"
                                     f"1st-Level Spell. You learn {spell.get_name()}. You always have "
                                     f"{spell.get_name()} prepared. You can cast it once without a Spell Slot, "
                                     f"and you regain the ability to cast it in that way when you finish a Long Rest. "
                                     f"You can also cast {spell.get_name()} using any Spell Slots you have.\n"
                                     f"{ability.value} is your spellcasting ability for these Spells.\n"
                                     "Whenever you gain a new level, you can replace one of the Spells you chose for "
                                     "this Feat with a different Spell of the same level from the chosen Spell list.",
                         repeatable="Yes, but you must choose a different Spell List each time",
                         spells=[cantrip1, cantrip2, spell])


class Musician(Feats.Feat):
    def __init__(self, instrument1: MusicalInstruments, instrument2: MusicalInstruments,
                 instrument3: MusicalInstruments):
        if instrument1 == instrument2 or instrument1 == instrument3 or instrument2 == instrument3:
            raise Exception("All 3 instruments should be unique")

        super().__init__(name="Musician",
                         level=1,
                         description="You are a practiced musician, granting you the following benefits:\n"
                                     f"Instrument Training. You gain Tool Proficiency with {instrument1.value}, "
                                     f"{instrument2.value}, and {instrument3.value}.\n"
                                     "Inspiring Song. As you finish a Short Rest or a Long Rest, you can play a song "
                                     "on a Musical Instrument with which you have Tool Proficiency and give "
                                     "Inspiration to allies who hear the song. The number of allies you can affect in "
                                     "this way equals your Proficiency Bonus.",
                         bonuses=Bonuses.Bonuses(musical_instruments={
                             instrument1: ProficiencyLevels.PROFICIENT,
                             instrument2: ProficiencyLevels.PROFICIENT,
                             instrument3: ProficiencyLevels.PROFICIENT,
                         }))


class SavageAttacker(Feats.Feat):
    def __init__(self):
        super().__init__(name="Savage Attacker",
                         level=1,
                         description="You have trained to deal particularly damaging strikes. When you take the "
                                     "Attack Action and hit a target with a Weapon as part of that Action, "
                                     "you can roll the Weapon’s damage dice twice and use either roll against the "
                                     "target. You can use this benefit only once per turn.")


class Skilled(Feats.Feat):
    def __init__(self, skill1: Skills, skill2: Skills, skill3: Skills):
        if skill1 == skill2 or skill1 == skill3 or skill2 == skill3:
            raise Exception("All 3 tools should be unique")

        super().__init__(name="Skilled",
                         level=1,
                         description=f"You have exceptionally broad learning. You gain Proficiency in {skill1.value}, "
                                     f"{skill2.value}, and {skill3.value}.",
                         repeatable="Yes",
                         bonuses=Bonuses.Bonuses(skills={
                             skill1: ProficiencyLevels.PROFICIENT,
                             skill2: ProficiencyLevels.PROFICIENT,
                             skill3: ProficiencyLevels.PROFICIENT,
                         }))


class TavernBrawler(Feats.Feat):
    def __init__(self):
        super().__init__(name="Tavern Brawler",
                         level=1,
                         description="Accustomed to brawling, you gain the following benefits:\n"
                                     "Enhanced Unarmed Strike. When you hit with your Unarmed Strike and deal damage, "
                                     "you can deal Bludgeoning Damage equal to 1d4 + your Strength modifier, instead "
                                     "of the normal damage of an Unarmed Strike.\n"
                                     "Damage Rerolls. Whenever you roll a damage die for your Unarmed Strike, "
                                     "you can reroll the die if it rolls a 1, and you must use the new roll.\n"
                                     "Shove. When you hit a creature with an Unarmed Strike as part of the Attack "
                                     "Action on your turn, you can deal damage to the target and also push it 5 feet "
                                     "away. You can use this benefit only once per turn.\n"
                                     "Furniture as Weapons. You can wield furniture as a Weapon, using the rules of "
                                     "the Greatclub for Small or Medium furniture and the rules of the Club for Tiny "
                                     "furniture.")


class Tough(Feats.Feat):
    def __init__(self):
        super().__init__(name="Tough",
                         level=1,
                         description="Your Hit Point Maximum increases by an amount equal to twice your character "
                                     "level when you gain this Feat. Whenever you gain a level thereafter, "
                                     "your Hit Point Maximum increases by an additional 2 Hit Points.",
                         bonuses=Bonuses.Bonuses(hp_bonus=True))


class Human(Races.Race):
    def __init__(self,
                 skill: Skills,
                 versatile: Feats.Feat,
                 size: Sizes = Sizes.MEDIUM):
        if size != Sizes.SMALL and size != Sizes.MEDIUM:
            raise Exception("Invalid Size")

        if versatile.get_level() != 1:
            raise Exception("Humans can only start with a first level Feat")

        super().__init__(name="Human",
                         features=[
                             Feats.Feat(name="Resourceful",
                                        description="You gain inspiration whenever you finish a Long Rest."),
                             Feats.Feat(name="Skillful",
                                        description=f"You gain proficiency in {skill.value}",
                                        bonuses=Bonuses.Bonuses(skills={
                                            skill: ProficiencyLevels.PROFICIENT
                                        })),
                             versatile,
                         ],
                         size=size,
                         life_span=80)


class Ardling(Races.Race):
    def __init__(self,
                 name: str,
                 size: Sizes,
                 celestial_legacy: Feats.Feat,
                 ability: AbilityNames):
        if size != Sizes.SMALL and size != Sizes.MEDIUM:
            raise Exception("Invalid Size")

        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception("Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             Feats.Feat(
                                 name="Angelic Flight",
                                 description="As a Bonus Action, you sprout spectral wings for a moment and fly up to "
                                             "a number of feet equal to your Speed. If you are in the air at the end "
                                             "of this movement,you fall if nothing is holding you aloft.\n"
                                             "You can use this Bonus Action a number of times equal to your "
                                             "Proficiency Bonus,and you regain all expended uses when you finish a "
                                             "Long Rest."
                             ),
                             celestial_legacy,
                             Feats.Feat(
                                 name="Damage Resistance",
                                 description="You have Resistance to Radiant Damage."
                             )
                         ],
                         size=size,
                         life_span=200)


class ExaltedArdling(Ardling):
    def __init__(self,
                 content,
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(name="Exalted Ardling",
                         size=size,
                         celestial_legacy=Feats.Feat(
                             name="Celestial Legacy",
                             description="You are the recipient of a celestial legacy that grants you magical "
                                         "abilities. Your Exalted legacy is associated with Chaotic Good planes. You "
                                         "gain the initial benefit of the chosen legacy: the Thaumaturgy cantrip.\n"
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Divine Favor and Lesser Restoration. "
                                         "Once you cast the Spell with this trait, you can’t cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Thaumaturgy"],
                                     content["Spells"]["Divine Favor"],
                                     content["Spells"]["Lesser Restoration"]]
                         ),
                         ability=ability)


class HeavenlyArdling(Ardling):
    def __init__(self,
                 content,
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(name="Heavenly Ardling",
                         size=size,
                         celestial_legacy=Feats.Feat(
                             name="Celestial Legacy",
                             description="You are the recipient of a celestial legacy that grants you magical "
                                         "abilities. Your Heavenly legacy is associated with Lawful Good planes. You "
                                         "gain the initial benefit of the chosen legacy: the Light cantrip.\n"
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Cure Wounds and Zone of Truth. "
                                         "Once you cast the Spell with this trait, you can’t cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Light"],
                                     content["Spells"]["Cure Wounds"],
                                     content["Spells"]["Zone of Truth"]]
                         ),
                         ability=ability)


class IdyllicArdling(Ardling):
    def __init__(self,
                 content,
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(name="Idyllic Ardling",
                         size=size,
                         celestial_legacy=Feats.Feat(
                             name="Celestial Legacy",
                             description="You are the recipient of a celestial legacy that grants you magical "
                                         "abilities. Your Idyllic legacy is associated with Neutral Good planes. You "
                                         "gain the initial benefit of the chosen legacy: the Guidance cantrip.\n"
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Healing Word and Animal Messenger. "
                                         "Once you cast the Spell with this trait, you can’t cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Guidance"],
                                     content["Spells"]["Healing Word"],
                                     content["Spells"]["Animal Messenger"]]
                         ),
                         ability=ability)


class Dragonborn(Races.Race):
    def __init__(self,
                 name: str,
                 ancestry: Feats.Feat,
                 damage_type: DamageTypes):
        super().__init__(name=name,
                         features=[
                             ancestry,
                             Feats.Feat(
                                 name="Breath Weapon",
                                 description="As an Action, you exhale destructive energy in a 15-foot cone. Each "
                                             "creature in that area must make a Dexterity saving throw against a DC "
                                             "equal to 8 + your Constitution modifier + your Proficiency Bonus. On a "
                                             "failed save, a creature takes 1d10 + your character level in damage of "
                                             f"{damage_type.value} damage. On a successful save, a creature takes half"
                                             "as much damage.\n"
                                             "You can use this Breath Weapon a number of times equal to your "
                                             "Proficiency Bonus,and you regain all expended uses when you finish a "
                                             "Long Rest."
                             ),
                             Feats.Feat(
                                 name="Damage Resistance",
                                 description=f"You have Resistance to {damage_type.value} damage."
                             ),
                             Feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             Feats.Feat(
                                 name="Draconic Language",
                                 description="You instinctively know the language of dragons. You can therefore speak, "
                                             "read, and write Draconic.",
                                 languages=[Languages.DRACONIC]
                             )
                         ],
                         life_span=80)


class BlackDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Black Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Black Dragon progenitor."
                         ),
                         damage_type=DamageTypes.ACID)


class BlueDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Blue Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Blue Dragon progenitor."
                         ),
                         damage_type=DamageTypes.LIGHTNING)


class BrassDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Brass Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Brass Dragon progenitor."
                         ),
                         damage_type=DamageTypes.FIRE)


class BronzeDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Bronze Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Bronze Dragon progenitor."
                         ),
                         damage_type=DamageTypes.LIGHTNING)


class CopperDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Copper Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Copper Dragon progenitor."
                         ),
                         damage_type=DamageTypes.ACID)


class GoldDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Gold Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Gold Dragon progenitor."
                         ),
                         damage_type=DamageTypes.FIRE)


class GreenDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Green Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Green Dragon progenitor."
                         ),
                         damage_type=DamageTypes.POISON)


class RedDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Red Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Red Dragon progenitor."
                         ),
                         damage_type=DamageTypes.FIRE)


class SilverDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="Silver Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Silver Dragon progenitor."
                         ),
                         damage_type=DamageTypes.COLD)


class WhiteDragonborn(Dragonborn):
    def __init__(self):
        super().__init__(name="White Dragonborn",
                         ancestry=Feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a White Dragon progenitor."
                         ),
                         damage_type=DamageTypes.COLD)


class Dwarf(Races.Race):
    def __init__(self, tool1: ArtisansTools, tool2: ArtisansTools):
        valid_tools = [ArtisansTools.JEWELERS_TOOLS, ArtisansTools.MASONS_TOOLS,
                       ArtisansTools.SMITHS_TOOLS, ArtisansTools.TINKERS_TOOLS]
        if tool1 not in valid_tools or tool2 not in valid_tools or tool1 == tool2:
            raise Exception("This tool selection is not valid")

        super().__init__(name="Dwarf",
                         features=[
                             Feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             Feats.Feat(
                                 name="Dwarven Resilience",
                                 description="You have Resistance to Poison Damage. You also have Advantage on saving "
                                             "throws you make to avoid or end the Poisoned Condition on yourself."
                             ),
                             Feats.Feat(
                                 name="Dwarven Toughness",
                                 description="Your Hit Point Maximum increases by 1, and it increases by 1 again "
                                             "whenever you gain a level.",
                                 bonuses=Bonuses.Bonuses(hp_bonus=1)
                             ),
                             Feats.Feat(
                                 name="Forge Wise",
                                 description="Your divine creator gave you an uncanny affinity for working with stone "
                                             f"or metal. You gain Tool Proficiency with {tool1.value} and "
                                             f"{tool2.value}."
                             ),
                             Feats.Feat(
                                 name="Stonecunning",
                                 description="As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 "
                                             "minutes. You must be on a stone surface or touching such a surface to "
                                             "use this Tremorsense. The stone can be natural or worked.\n"
                                             "You can use this Bonus Action a number of times equal to your "
                                             "Proficiency Bonus, and you regain all expended uses when you finish a "
                                             "Long Rest."
                             )
                         ],
                         life_span=350)


class Elf(Races.Race):
    def __init__(self,
                 name: str,
                 lineage: Feats.Feat,
                 ability: AbilityNames,
                 darkvision: Feats.Feat = Feats.Feat(
                     name="Darkvision",
                     description="You have Darkvision with a range of 60 feet."
                 ),
                 speed: int = 30):
        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception("Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             darkvision,
                             lineage,
                             Feats.Feat(
                                 name="Fey Ancestry",
                                 description="You have Advantage on saving throws you make to avoid or end the "
                                             "Charmed Condition on yourself."
                             ),
                             Feats.Feat(
                                 name="Keen Senses",
                                 description="You have Proficiency in the Perception Skill.",
                                 bonuses=Bonuses.Bonuses(skills={Skills.PERCEPTION: ProficiencyLevels.PROFICIENT})
                             ),
                             Feats.Feat(
                                 name="Trance",
                                 description="You don’t need to sleep,and magic can’t put you to sleep.You can finish "
                                             "a Long Rest in 4 hours if you spend those hours in a trancelike "
                                             "meditation, during which you retain consciousness."
                             )
                         ],
                         speed=speed,
                         life_span=750)


class Drow(Elf):
    def __init__(self,
                 content,
                 ability: AbilityNames):
        super().__init__(name="Drow",
                         lineage=Feats.Feat(
                             name="Elven Lineage",
                             description="You are part of an elven lineage that grants you supernatural abilities. "
                                         "Your Drow lineage is of the Underdark. You know the Dancing Lights cantrip.\n"
                                         "Starting at 3rd level and again at 5th level, you also gain the ability to "
                                         "cast a Spell with this trait, Faerie Fire and Darkness. Once you cast the "
                                         "Spell with this trait, you can’t cast that Spell with it again until you "
                                         "finish a Long Rest; however, you can cast the Spell using any Spell Slots "
                                         "you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Dancing Lights"],
                                     content["Spells"]["Faerie Fire"],
                                     content["Spells"]["Darkness"]]
                         ),
                         ability=ability,
                         darkvision=Feats.Feat(
                             name="Darkvision",
                             description="You have Darkvision with a range of 120 feet."
                         ))


class HighElf(Elf):
    def __init__(self,
                 content,
                 ability: AbilityNames):
        super().__init__(name="High Elf",
                         lineage=Feats.Feat(
                             name="Elven Lineage",
                             description="You are part of an elven lineage that grants you supernatural abilities. "
                                         "Your High Elf lineage is of fey crossings and other magical locations. "
                                         "You know the Prestidigitation cantrip. Whenever you finish a Long Rest, "
                                         "you can replace that cantrip with a different cantrip from the Arcane Spell "
                                         "List.\n"
                                         "Starting at 3rd level and again at 5th level, you also gain the ability to "
                                         "cast a Spell with this trait, Detect Magic and Misty Step. Once you cast the "
                                         "Spell with this trait, you can’t cast that Spell with it again until you "
                                         "finish a Long Rest; however, you can cast the Spell using any Spell Slots "
                                         "you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Prestidigitation"],
                                     content["Spells"]["Detect Magic"],
                                     content["Spells"]["Misty Step"]]
                         ),
                         ability=ability)


class WoodElf(Elf):
    def __init__(self,
                 content,
                 ability: AbilityNames):
        super().__init__(name="Wood Elf",
                         lineage=Feats.Feat(
                             name="Elven Lineage",
                             description="You are part of an elven lineage that grants you supernatural abilities. "
                                         "Your Wood Elf lineage is of primeval forests. Your Speed increases to 35 "
                                         "feet. You know the Druidcraft cantrip.\n "
                                         "Starting at 3rd level and again at 5th level, you also gain the ability to "
                                         "cast a Spell with this trait, Longstrider and Pass Without Trace. Once you "
                                         "cast the Spell with this trait, you can’t cast that Spell with it again "
                                         "until you finish a Long Rest; however, you can cast the Spell using any "
                                         "Spell Slots you have of the appropriate level.\n "
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Druidcraft"],
                                     content["Spells"]["Longstrider"],
                                     content["Spells"]["Pass Without Trace"]]
                         ),
                         ability=ability)


class Gnome(Races.Race):
    def __init__(self,
                 name: str,
                 lineage: Feats.Feat,
                 ability: AbilityNames):
        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception("Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             Feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             Feats.Feat(
                                 name="Gnomish Cunning",
                                 description="You have Advantage on Intelligence, Wisdom, and Charisma saving throws."
                             ),
                             lineage
                         ],
                         size=Sizes.SMALL,
                         life_span=425)


class ForestGnome(Gnome):
    def __init__(self,
                 content,
                 ability: AbilityNames):
        super().__init__(name="Forest Gnome",
                         lineage=Feats.Feat(
                             name="Gnomish Lineage",
                             description="You are part of a gnomish lineage that grants you supernatural abilities. "
                                         "Your Forest lineage is of magic-filled forests. You know the Minor Illusion "
                                         "cantrip.\n "
                                         "You can also cast the Speak with Animals Spell with this trait. You can "
                                         "cast it with the trait a number of times equal to your Proficiency Bonus, "
                                         "and you regain all expended uses when you finish a Long Rest. You can also "
                                         "use any Spell Slots you have to cast the Spell.",
                             spells=[content["Spells"]["Minor Illusion"],
                                     content["Spells"]["Speak with Animals"]]
                         ),
                         ability=ability)


class RockGnome(Gnome):
    def __init__(self,
                 content,
                 ability: AbilityNames):
        super().__init__(name="Rock Gnome",
                         lineage=Feats.Feat(
                             name="Gnomish Lineage",
                             description="You are part of a gnomish lineage that grants you supernatural abilities. "
                                         "Your Rock lineage is of primeval mountains. You know the Mending and "
                                         "Prestidigitation cantrips.\n "
                                         "In addition, you can spend 10 minutes casting Prestidigitation to create a "
                                         "Tiny clockwork device (AC 5, 1 HP), such as a toy, a fire starter, "
                                         "or a music box. Casting the Spell in this way consumes 10 GP worth of raw "
                                         "material (string, gears, and the like), which you provide during the "
                                         "casting.\n"
                                         "When you create the device, you determine its function by choosing one "
                                         "effect from Prestidigitation; the device produces that effect whenever you "
                                         "or another creature takes a Bonus Action to touch the device and activate "
                                         "it. If the chosen effect has options within it, you choose one of those "
                                         "options for the device when you create it. For example, if you choose the "
                                         "spell’s ignite-extinguish effect, you determine whether the device ignites "
                                         "or extinguishes fire; the device doesn't do both.\n"
                                         "You can have three such devices in existence at a time, and each one "
                                         "dismantles itself 8 hours after its creation. You can also touch one of "
                                         "your devices and dismantle it as an Action. After a device is dismantled, "
                                         "the 10 GP of materials used to create it can be reclaimed.",
                             spells=[content["Spells"]["Mending"],
                                     content["Spells"]["Prestidigitation"]]
                         ),
                         ability=ability)


class Halfling(Races.Race):
    def __init__(self):
        super().__init__(name="Halfling",
                         features=[
                             Feats.Feat(
                                 name="Brave",
                                 description="You have Advantage on saving throws you make to avoid or end the "
                                             "Frightened Condition on yourself."
                             ),
                             Feats.Feat(
                                 name="Halfling Nimbleness",
                                 description="You can move through the space of any creature that is of a Size larger "
                                             "than yours, but you can’t stop there."
                             ),
                             Feats.Feat(
                                 name="Luck",
                                 description="When your oll a 1 on the d20 of a d20 Test, you can reroll the die, "
                                             "and you must use the new roll."
                             ),
                             Feats.Feat(
                                 name="Naturally Stealthy",
                                 description="You have Proficiency in the Stealth Skill.",
                                 bonuses=Bonuses.Bonuses(skills={Skills.STEALTH: ProficiencyLevels.PROFICIENT})
                             )
                         ],
                         size=Sizes.SMALL,
                         life_span=150)


class Orc(Races.Race):
    def __init__(self):
        super().__init__(name="Orc",
                         features=[
                             Feats.Feat(
                                 name="Adrenaline Rush",
                                 description="You can take the Dash Action as a Bonus Action. When you do so,you gain "
                                             "a number of Temporary Hit Points equal to your Proficiency Bonus.\n"
                                             "You can use this trait a number of times equal to your Proficiency "
                                             "Bonus, and you regain all expended uses when you finish a Long Rest."
                             ),
                             Feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             Feats.Feat(
                                 name="Powerful Build",
                                 description="You count as one Size larger when determining your carrying capacity "
                                             "and the weight you can push, drag, or lift."
                             ),
                             Feats.Feat(
                                 name="Relentless Endurance",
                                 description="When you are reduced to 0 Hit Points but not killed outright, you can "
                                             "drop to 1 Hit Point instead. Once you use this trait,you can’t do so "
                                             "again until you finish a Long Rest"
                             )
                         ],
                         life_span=80)


class Tiefling(Races.Race):
    def __init__(self,
                 content,
                 name: str,
                 size: Sizes,
                 fiendish_legacy: Feats.Feat,
                 ability: AbilityNames):
        if size != Sizes.SMALL and size != Sizes.MEDIUM:
            raise Exception("Invalid Size")

        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception("Spellcasting ability must be one of the mental abilities.")

        super().__init__(name=name,
                         features=[
                             Feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             fiendish_legacy,
                             Feats.Feat(
                                 name="Otherworldly Presence",
                                 description="You know the Thaumaturgy cantrip. When you cast it with this trait,"
                                             f"the Spell uses {ability.value}.",
                                 spells=[content["Spells"]["Thaumaturgy"]]
                             )
                         ],
                         size=size)


class AbyssalTiefling(Tiefling):
    def __init__(self,
                 content,
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(content=content,
                         name="Abyssal Tiefling",
                         size=size,
                         fiendish_legacy=Feats.Feat(
                             name="Fiendish Legacy",
                             description="You are the recipient of a fiendish legacy that grants you supernatural  "
                                         "abilities. Your Abyssal legacy is associated with Chaotic Evil planes. You "
                                         "gain the 1st-level benefit of the chosen legacy: the Poison Spray cantrip "
                                         "and resistance to Poison damage.\n "
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Ray of Sickness and Hold Person. "
                                         "Once you cast the Spell with this trait, you can’t cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Poison Spray"],
                                     content["Spells"]["Ray of Sickness"],
                                     content["Spells"]["Hold Person"]]
                         ),
                         ability=ability)


class ChthonicTiefling(Tiefling):
    def __init__(self,
                 content,
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(content=content,
                         name="Chthonic Tiefling",
                         size=size,
                         fiendish_legacy=Feats.Feat(
                             name="Fiendish Legacy",
                             description="You are the recipient of a fiendish legacy that grants you supernatural  "
                                         "abilities. Your Chthonic legacy is associated with Neutral Evil planes. You "
                                         "gain the 1st-level benefit of the chosen legacy: the Chill Touch cantrip "
                                         "and resistance to Necrotic damage.\n "
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, False Life and Ray of Enfeeblement. "
                                         "Once you cast the Spell with this trait, you can’t cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Chill Touch"],
                                     content["Spells"]["False Life"],
                                     content["Spells"]["Ray of Enfeeblement"]]
                         ),
                         ability=ability)


class InfernalTiefling(Tiefling):
    def __init__(self,
                 content,
                 ability: AbilityNames,
                 size: Sizes = Sizes.MEDIUM):
        super().__init__(content=content,
                         name="Infernal Tiefling",
                         size=size,
                         fiendish_legacy=Feats.Feat(
                             name="Fiendish Legacy",
                             description="You are the recipient of a fiendish legacy that grants you supernatural  "
                                         "abilities. Your Infernal legacy is associated with Lawful Evil planes. You "
                                         "gain the 1st-level benefit of the chosen legacy: the Fire Bolt cantrip "
                                         "and resistance to Fire damage.\n "
                                         "Starting at 3rd level and again at 5th level, you gain the ability to cast "
                                         "a higher-level Spell with this trait, Hellish Rebuke and Darkness. "
                                         "Once you cast the Spell with this trait, you can’t cast that Spell with it "
                                         "again until you finish a Long Rest; however, you can cast the Spell using "
                                         "any Spell Slots you have of the appropriate level.\n"
                                         f"{ability.value} is your spellcasting ability for the Spells you cast with "
                                         "this trait.",
                             spells=[content["Spells"]["Fire Bolt"],
                                     content["Spells"]["Hellish Rebuke"],
                                     content["Spells"]["Darkness"]]
                         ),
                         ability=ability)


CONTENT = {
    "Backgrounds": {
        "Custom": Backgrounds.Background,
        # TODO
        # "Artisan": Artisan,
        # "Charlatan": Charlatan,
        # "Criminal": Criminal,
        # "Cultist": Cultist,
        # "Entertainer": Entertainer,
        # "Farmer": Farmer,
        # "Gladiator": Gladiator,
        # "Guard": Guard,
        # "Guide": Guide,
        # "Hermit": Hermit,
        # "Laborer": Laborer,
        # "Noble": Noble,
        # "Pilgrim": Pilgrim,
        # "Sage": Sage,
        # "Sailor": Sailor,
        # "Soldier": Soldier,
        # "Urchin": Urchin,
    },
    "Feats": {
        "Alert": Alert,
        "Crafter": Crafter,
        "Healer": Healer,
        "Lucky": Lucky,
        "Magic Initiate": MagicInitiate,
        "Musician": Musician,
        "Savage Attacked": SavageAttacker,
        "Skilled": Skilled,
        "Tavern Brawler": TavernBrawler,
        "Tough": Tough,
    },
    "Races": {
        "Human": Human,
        "Exalted Ardling": ExaltedArdling,
        "Heavenly Ardling": HeavenlyArdling,
        "Idyllic Ardling": IdyllicArdling,
        "Black Dragonborn": BlackDragonborn,
        "Blue Dragonborn": BlueDragonborn,
        "Brass Dragonborn": BrassDragonborn,
        "Bronze Dragonborn": BronzeDragonborn,
        "Copper Dragonborn": CopperDragonborn,
        "Gold Dragonborn": GoldDragonborn,
        "Green Dragonborn": GreenDragonborn,
        "Red Dragonborn": RedDragonborn,
        "Silver Dragonborn": SilverDragonborn,
        "White Dragonborn": WhiteDragonborn,
        "Dwarf": Dwarf,
        "Drow": Drow,
        "High Elf": HighElf,
        "Wood Elf": WoodElf,
        "Forest Gnome": ForestGnome,
        "Rock Gnome": RockGnome,
        "Halfling": Halfling,
        "Orc": Orc,
        "Abyssal Tiefling": AbyssalTiefling,
        "Chthonic Tiefling": ChthonicTiefling,
        "Infernal Tiefling": InfernalTiefling,
    },
}
