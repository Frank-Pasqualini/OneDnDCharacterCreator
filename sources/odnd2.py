"""
Content from the Dungeons and Dragons OneD&D Expert Classes Unearthed Arcana.
https://media.dndbeyond.com/compendium-images/one-dnd/expert-classes/kpx0MvyfBGHe0XKk/UA2022-Expert-Classes.pdf
"""

from rules import abilities, bonuses, classes, feats, spells
from rules.enums import AbilityNames, DamageTypes, ProficiencyLevels, Skills, SpellLists, SpellSchools


class HunterRanger(classes.Ranger):
    """
    Thief subclass for Rogue
    UA p. 15
    """

    def __init__(self, **kwargs):
        super().__init__(name="Hunter Ranger", **kwargs)

    def _level_up_3(self):
        self._features.append(feats.Feat(name="Hunter's Prey",
                                         description="Your tenacity can wear down even the most resilient foes. When "
                                                     "you hit a creature with a Weapon or an Unarmed Strike as part "
                                                     "of the Attack Action on your turn, the Weapon or Unarmed Strike "
                                                     "deals an extra 1d8 damage to the target if it's missing any of "
                                                     "its Hit Points. You can deal this extra damage only once per "
                                                     "turn."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Hunter's Lore",
                                         description="You can call on the forces of nature to reveal certain "
                                                     "strengths and weaknesses of your prey. While a creature is "
                                                     "marked by your Hunter's Mark,you know whether that creature has "
                                                     "any Immunities,Resistances, and Vulnerabilities, and if the "
                                                     "creature has any,you know what they are."))

    def _level_up_10(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Multiattack",
                                         description="You now always have Conjure Barrage prepared, and it doesn't "
                                                     "count against the number of Spells you can prepare.\n"
                                                     "You can also cast the Spell with 1st- and 2nd-level Spell "
                                                     "Slots. When you do so,the Spell's damage is reduced by 1d8 for "
                                                     "each slot level below 3rd.",
                                         feat_spells=[
                                             content["Spells"]["Conjure Barrage"]],
                                         spellcasting_ability=AbilityNames.WISDOM))

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Superior Hunter's Defense",
                                         description="When you are hit by an Attack Roll,you can use your Reaction to "
                                                     "halve the attack's damage against yourself,and you can redirect "
                                                     "the other half of the damage to one creature (other than the "
                                                     "attacker) that you can see within 5 feet of yourself."))


class LoreBard(classes.Bard):
    """
    Thief subclass for Rogue
    UA p. 7
    """

    def _level_up_3(self):
        self._features.append(feats.Feat(name="Bonus Proficiencies",
                                         description="You gain three Skill Proficiencies: Arcana, History, "
                                                     "and Nature. If you already have one of these Proficiencies, "
                                                     "choose a Skill Proficiency you lack, and gain that Proficiency.",
                                         feat_bonuses=bonuses.Bonuses(skills={
                                             Skills.ARCANA: ProficiencyLevels.PROFICIENT,
                                             Skills.HISTORY: ProficiencyLevels.PROFICIENT,
                                             Skills.NATURE: ProficiencyLevels.PROFICIENT,
                                         }),
                                         visible=False))

        self._features.append(feats.Feat(name="Cutting Words",
                                         description="You learn how to use your wit to supernaturally distract, "
                                                     "confuse, and otherwise sap the confidence and competence of "
                                                     "others. When a creature that you can see within 60 feet of "
                                                     "yourself succeeds on an Ability Check or an Attack Roll, "
                                                     "you can use your Reaction to expend one of your uses of Bardic "
                                                     "Inspiration, rolling a Bardic Inspiration die and subtracting "
                                                     "the number rolled from the creature's roll, potentially turning "
                                                     "it into a failure."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Cunning Inspiration",
                                         description="Through your studies and your cunning, you've learned to "
                                                     "inspire others exceptionally well. When any creature rolls your "
                                                     "Bardic Inspiration die, that creature can roll the die twice "
                                                     "and use the higher of the two rolls."))

    def _level_up_10(self):
        self._features.append(feats.Feat(name="Improved Cutting Words",
                                         description="Whenever you use your Cutting Words feature on a creature, "
                                                     "you can deal Psychic Damage to that creature equal to the "
                                                     "number rolled on the Bardic Inspiration die plus your Charisma "
                                                     "modifier."))

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Peerless Skill",
                                         description="When you make an Ability Check and fail,you can expend one use "
                                                     "of Bardic Inspiration, roll the Bardic Inspiration die, "
                                                     "and add the number rolled to the Ability Check, potentially "
                                                     "turning it into a success. If the check still fails, "
                                                     "the Bardic Inspiration isn't expended."))


class ThiefRogue(classes.Rogue):
    """
    Thief subclass for Rogue
    UA p. 15
    """

    def __init__(self, **kwargs):
        super().__init__(name="Thief Rogue", **kwargs)

    def _level_up_3(self):
        self._features.append(feats.Feat(name="Fast Hands",
                                         description="You have additional options for the Bonus Action of your "
                                                     "Cunning Action, with which you can do the following:\n"
                                                     "Search. Take the Search Action.\n"
                                                     "Sleight of Hand. Make a Dexterity Check (Sleight of Hand) to "
                                                     "pick a lock or disarm a trap with Thieves' Tools or to pick a "
                                                     "pocket."))
        self._features.append(feats.Feat(name="Second-Story Work",
                                         description="You have trained to reach especially hard-to-reach places, "
                                                     "granting you these benefits:\n"
                                                     "Climb Speed. You gain a Climb Speed equal to your Speed.\n"
                                                     "Jump Distance. When you take the Jump Action, you can make a "
                                                     "Dexterity Check, instead of a Strength Check."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Supreme Sneak",
                                         description="You have Advantage on every Dexterity Check (Stealth) you make, "
                                                     "provided you aren't wearing Medium or Heavy Armor."))

    def _level_up_10(self, **kwargs):
        super()._level_up_10(**kwargs)
        self._features.append(feats.Feat(name="Use Magic Device",
                                         description="In your treasure hunting,you have learned how to maximize use "
                                                     "of magic items, granting you the following benefits:\n"
                                                     "Attunement. You can attune to up to four magic items at once.\n"
                                                     "Charges. Whenever you use a magic item property that expends "
                                                     "charges, roll a d6. On a roll of 6, you use the property "
                                                     "without expending the charges.\n"
                                                     "Scrolls. You can use any Spell Scroll that bears a cantrip or a "
                                                     "1st-level Spell. You can also try to use any Spell Scroll that "
                                                     "contains a higher-level Spell, but you must first succeed on an "
                                                     "Intelligence Check (Arcana) with a DC equal to 10 + the Spell's "
                                                     "level. On a successful check, you cast the Spell from the "
                                                     "scroll, and you use Intelligence as your Spellcasting Ability "
                                                     "for this casting. On a failed check, the scroll disintegrates."))

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Thief's Reflexes",
                                         description="You can now take a second Bonus Action on your turn, provided "
                                                     "it is the Bonus Action from Cunning Action. You can use this "
                                                     "feature on a number of turns equal to your Proficiency Bonus,"
                                                     "and you regain all expended uses when you finish a Long Rest."))


class AbilityScoreImprovement(feats.Feat):
    """
    Ability Score Improvement Feat
    UA p. 16
    """

    def __init__(self, ability1: AbilityNames, ability2: AbilityNames):
        if ability1 == ability2:
            super().__init__(name="Ability Score Improvement",
                             description=f"You increase {ability1.value} by 2.",
                             level=4,
                             repeatable="Yes",
                             feat_abilities=abilities.Abilities(
                                 strength=2 if ability1 == AbilityNames.STRENGTH else 0,
                                 dexterity=2 if ability1 == AbilityNames.DEXTERITY else 0,
                                 constitution=2 if ability1 == AbilityNames.CONSTITUTION else 0,
                                 intelligence=2 if ability1 == AbilityNames.INTELLIGENCE else 0,
                                 wisdom=2 if ability1 == AbilityNames.WISDOM else 0,
                                 charisma=2 if ability1 == AbilityNames.CHARISMA else 0,
                             ),
                             visible=False)
        else:
            super().__init__(name="Ability Score Improvement",
                             description=f"You increase {ability1.value} and {ability2.value} by 1.",
                             level=4,
                             repeatable="Yes",
                             feat_abilities=abilities.Abilities(
                                 strength=(1 if AbilityNames.STRENGTH in [
                                     ability1, ability2] else 0),
                                 dexterity=(1 if AbilityNames.DEXTERITY in [
                                     ability1, ability2] else 0),
                                 constitution=(1 if AbilityNames.CONSTITUTION in [
                                     ability1, ability2] else 0),
                                 intelligence=(1 if AbilityNames.INTELLIGENCE in [
                                     ability1, ability2] else 0),
                                 wisdom=(1 if AbilityNames.WISDOM in [
                                     ability1, ability2] else 0),
                                 charisma=(1 if AbilityNames.CHARISMA in [ability1, ability2] else 0)),
                             visible=False)


class Actor(feats.Feat):
    """
    Actor Feat
    UA p. 16
    """

    def __init__(self):
        super().__init__(name="Actor",
                         level=4,
                         prerequisite="Charisma 13+",
                         description="Skilled at mimicry and dramatics, you gain the following benefits:\n"
                                     "Ability Score Increase. Increase your Charisma score by 1, to a maximum of 20.\n"
                                     "Impersonation. While you're disguised as a fictional person or a real person "
                                     "other than yourself, you have Advantage on Charisma Checks (Performance) to "
                                     "convince others that you are that person.\n"
                                     "Mimicry. You can mimic the sounds of other creatures,including speech. To mimic "
                                     "a sound or a way of speaking, you must listen to it for at least 1 minute. Any "
                                     "time thereafter, you can make a DC15Charisma Check (Performance) to perform the "
                                     "mimicry; on a success, you perform it convincingly for up to 1 hour.",
                         feat_abilities=abilities.Abilities(charisma=1))


class Athlete(feats.Feat):
    """
    Athlete Feat
    UA p. 16
    """

    def __init__(self, ability: AbilityNames):
        if ability not in [AbilityNames.STRENGTH, AbilityNames.DEXTERITY, AbilityNames.CONSTITUTION]:
            raise Exception(
                "Ability must be Strength, Dexterity, or Constitution")

        super().__init__(name="Athlete",
                         level=4,
                         prerequisite="Strength, Dexterity,or Constitution 13+",
                         description="You have undergone extensive physical training to gain the following benefits:\n"
                                     f"Ability Score Increase. Increase your {ability.value} score by 1, to a maximum "
                                     "of 20.\n"
                                     "Climb Speed. You gain a Climb Speed equal to your Speed.\n"
                                     "Hop Up. When you are Prone, you can right yourself with only 5 feet of "
                                     "movement.\n"
                                     "Jumping. You have Advantage on any Ability Check you make for the Jump Action.",
                         feat_abilities=abilities.Abilities(
                             strength=(
                                 1 if AbilityNames.STRENGTH == ability else 0),
                             dexterity=(
                                 1 if AbilityNames.DEXTERITY == ability else 0),
                             constitution=(1 if AbilityNames.CONSTITUTION == ability else 0)))


class Charger(feats.Feat):
    """
    Charger Feat
    UA p. 16
    """

    def __init__(self, ability: AbilityNames):
        if ability not in [AbilityNames.STRENGTH, AbilityNames.DEXTERITY]:
            raise Exception("Ability must be Strength or Dexterity")

        super().__init__(name="Charger",
                         level=4,
                         prerequisite="Proficiency with Any Martial Weapon",
                         description="You have trained to charge headlong into battle, gaining the following "
                                     "benefits:\n"
                                     f"Ability Score Increase. Increase your {ability.value} score by 1, to a maximum "
                                     "of 20.\n"
                                     "Improved Dash. When you take the Dash Action,your Speed increases by 10 feet for "
                                     "that Action.\n"
                                     "Charge Attack. If you move at least 10 feet in a straight line immediately "
                                     "before hitting with an attack as part of the Attack Action on your turn, "
                                     "choose one of the following effects: gain a +1d8 bonus to the attack's damage "
                                     "roll, or push the target up to 10 feet,provided the target you want to push is "
                                     "no more than one Size larger than you. You can use this benefit only once on "
                                     "each of your turns.",
                         feat_abilities=abilities.Abilities(
                             strength=(
                                 1 if AbilityNames.STRENGTH == ability else 0),
                             dexterity=(1 if AbilityNames.DEXTERITY == ability else 0)))


class CrossbowExpert(feats.Feat):
    """
    Crossbow Expert Feat
    UA p. 16
    """

    def __init__(self):
        super().__init__(name="Crossbow Expert",
                         level=4,
                         prerequisite="Proficiency with Any Martial Weapon",
                         description="Thanks to extensive practice with crossbows, you gain the following benefits:\n"
                                     "Ability Score Increase. Increase your Dexterity score by 1, to a maximum of 20.\n"
                                     "Ignore Loading. You ignore the Loading property of crossbows.\n"
                                     "Firing in Melee. Being within 5 feet of an enemy doesn't impose Disadvantage on "
                                     "your Attack Rolls with crossbows.\n "
                                     "Dual Wielding. When you make the extra attack of the Light weapon property,"
                                     "you can add your Ability Modifier to the damage of the extra attack if that "
                                     "attack is with a crossbow that has the Light property.",
                         feat_abilities=abilities.Abilities(dexterity=1))


class DefensiveDuelist(feats.Feat):
    """
    Defensive Duelist Feat
    UA p. 16
    """

    def __init__(self):
        super().__init__(name="Defensive Duelist",
                         level=4,
                         prerequisite="Dexterity 13+",
                         description="You've learned to deftly parry attacks, granting you the following benefits:\n"
                                     "Ability Score Increase. Increase your Dexterity score by 1, to a maximum of 20.\n"
                                     "Parry. If you are holding a Finesse Weapon and another creature hits you with a "
                                     "Melee Attack, you can use your Reaction to add your Proficiency Bonus to your "
                                     "Armor Class for that attack, potentially causing the attack to miss you.",
                         feat_abilities=abilities.Abilities(dexterity=1))


class DualWielder(feats.Feat):
    """
    Dual Wielder Feat
    UA p. 16
    """

    def __init__(self, ability: AbilityNames):
        if ability not in [AbilityNames.STRENGTH, AbilityNames.DEXTERITY]:
            raise Exception("Ability must be Strength or Dexterity")

        super().__init__(name="Dual Wielder",
                         level=4,
                         prerequisite="Proficiency with Any Martial Weapon",
                         description="You master fighting with two weapons, gaining the following benefits:\n"
                                     f"Ability Score Increase. Increase your {ability.value} score by 1, to a maximum "
                                     "of 20.\n"
                                     "Enhanced Dual Wielding. When you are holding a Weapon with the Light property "
                                     "in one hand, you can treat a non-Light Weapon in your other hand as if it had "
                                     "the Light property, provided that Weapon lacks the Two-Handed property.\n "
                                     "Quick Draw. You can draw or stow two Weapons that lack the Two-Handed property "
                                     "when you would normally be able to draw or stow only one.",
                         feat_abilities=abilities.Abilities(
                             strength=(
                                 1 if AbilityNames.STRENGTH == ability else 0),
                             dexterity=(1 if AbilityNames.DEXTERITY == ability else 0)))


class Durable(feats.Feat):
    """
    Durable Feat
    UA p. 16
    """

    def __init__(self):
        super().__init__(name="Durable",
                         level=4,
                         prerequisite="Constitution 13+",
                         description="Hardy and resilient, you gain the following benefits:\n"
                                     "Ability Score Increase. Increase your Constitution score by 1, to a maximum of "
                                     "20.\n"
                                     "Defy Death. You have Advantage on Death Saving Throws.\n"
                                     "Speedy Recovery. As a Bonus Action, you can expend one of your Hit Dice, "
                                     "roll the die, and regain a number of Hit Points equal to the roll.",
                         feat_abilities=abilities.Abilities(constitution=1))


class ElementalAdept(feats.Feat):
    """
    Elemental Adept Feat
    UA p. 16
    """

    def __init__(self, ability: AbilityNames, damage_type: DamageTypes):
        if ability not in [AbilityNames.INTELLIGENCE, AbilityNames.WISDOM, AbilityNames.CHARISMA]:
            raise Exception(
                "Ability must be Strength, Dexterity, or Constitution")

        if damage_type not in [DamageTypes.ACID, DamageTypes.COLD, DamageTypes.FIRE, DamageTypes.LIGHTNING,
                               DamageTypes.THUNDER]:
            raise Exception(
                "Damage type must be Acid, Cold, Fire, Lightning, or Thunder")

        super().__init__(name="Elemental Adept",
                         level=4,
                         prerequisite="Spellcasting or Pact Magic Feature",
                         repeatable="Yes, but you must choose a different Damage Type each time for Energy Mastery",
                         description="In your spellcasting,you can harness a particular form of energy with deadly "
                                     "mastery, granting you the following benefits:\n"
                                     f"Ability Score Increase. Increase your {ability.value} score by 1, to a maximum "
                                     "of 20.\n"
                                     f"Energy Mastery. Spells you cast ignore Resistance to {damage_type.value} "
                                     "damage. In addition, when you roll damage for a Spell you cast that deals "
                                     "damage of that type, you can treat any 1 on a damage die as a 2.",
                         feat_abilities=abilities.Abilities(
                             intelligence=(
                                 1 if AbilityNames.INTELLIGENCE == ability else 0),
                             wisdom=(
                                 1 if AbilityNames.WISDOM == ability else 0),
                             charisma=(1 if AbilityNames.CHARISMA == ability else 0)))


class FightingStyleArchery(feats.FightingStyle):
    """
    Fighting Style: Archery Feat
    UA p. 19
    """

    def __init__(self):
        super().__init__(name="Fighting Style: Archery",
                         level=1,
                         prerequisite="Warrior Group",
                         description="You gain a +2 bonus to Attack Rolls you make with Ranged Weapons.",
                         feat_bonuses=bonuses.Bonuses())  # TODO implement ranged attack bonus


class FightingStyleDefense(feats.FightingStyle):
    """
    Fighting Style: Defense Feat
    UA p. 19
    """

    def __init__(self):
        super().__init__(name="Fighting Style: Archery",
                         level=1,
                         prerequisite="Warrior Group",
                         description="While you are wearing armor, you gain a +1 bonus to Armor Class.",
                         feat_bonuses=bonuses.Bonuses())  # TODO implement AC bonus


class FightingStyleGreatWeapon(feats.FightingStyle):
    """
    Fighting Style: Great Weapon Fighting Feat
    UA p. 19
    """

    def __init__(self):
        super().__init__(name="Fighting Style: Great Weapon Fighting",
                         level=1,
                         prerequisite="Warrior Group",
                         description="When you roll a 1 or 2 on a damage die for an attack you make with a Melee "
                                     "Weapon that you are wielding with two hands, you can reroll the die, "
                                     "and you must use the new roll. The Weapon must have the Two-Handed or Versatile "
                                     "property to gain this benefit.")


class Barkskin(spells.Spell):
    """
    Barkskin Spell
    UA p. 31
    """

    def __init__(self):
        super().__init__(name="Barkskin",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="Bonus Action",
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a handful of bark",
                         concentration=True,
                         duration="1 hour",
                         description="You touch one willing creature to protect it with regenerating bark. Until the "
                                     "Spell ends, the target's skin assumes a bark-like appearance, and at the start "
                                     "of each of the target's turns, the target gains a number of Temporary Hit "
                                     "Points equal to your Spellcasting Ability Modifier plus your Proficiency Bonus.",
                         at_higher_levels="When you cast this Spell using a Spell Slot of 3rd level or higher, "
                                          "you can target one additional willing creature for each slot level above "
                                          "2nd.")


class Guidance(spells.Spell):
    """
    Guidance Spell
    UA p. 32-33
    """

    def __init__(self):
        super().__init__(name="Guidance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.DIVINATION,
                         casting_time="Reaction, which you take in response to you or an ally within 30 feet of you "
                                      "failing an Ability Check",
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You channel magical insight to the creature who failed the Ability Check. That "
                                     "creature can roll a d4 and add the number rolled to the check, potentially "
                                     "turning it into a success.\n"
                                     "Once a creature rolls the die for this Spell, that creature can't benefit from "
                                     "the Spell again until the creature finishes a Long Rest.")


CONTENT = {
    "Classes": {
        "Hunter Ranger": HunterRanger,
        "Lore Bard": LoreBard,
        "Thief Rogue": ThiefRogue,
    },
    "Feats": {
        # TODO The rest of the feats
        "Ability Score Improvement": AbilityScoreImprovement,
        "Actor": Actor,
        "Athlete": Athlete,
        "Charger": Charger,
        "Crossbow Expert": CrossbowExpert,
        "Defensive Duelist": DefensiveDuelist,
        "Dual Wielder": DualWielder,
        "Durable": Durable,
        "Elemental Adept": ElementalAdept,
        # "Epic Boon of Combat Prowess": EpicBoonCombatProwess,
        # "Epic Boon of Dimensional Travel": EpicBoonDimensionalTravel,
        # "Epic Boon of Energy Resistance": EpicBoonEnergyResistance,
        # "Epic Boon of Fortitude": EpicBoonFortitude,
        # "Epic Boon of Irresistible Offense": EpicBoonIrresistibleOffense,
        # "Epic Boon of Luck": EpicBoonLuck,
        # "Epic Boon of the Night Spirit": EpicBoonNightSpirit,
        # "Epic Boon of Peerless Aim": EpicBoonPeerlessAim,
        # "Epic Boon of Recovery": EpicBoonRecovery,
        # "Epic Boon of Skill Proficiency": EpicBoonSkillProficiency,
        # "Epic Boon of Speed": EpicBoonSpeed,
        # "Epic Boon of Undetectability": EpicBoonUndetectability,
        # "Epic Boon of the Unfettered": EpicBoonUnfettered,
        "Fighting Style: Archery": FightingStyleArchery,
        "Fighting Style: Defense": FightingStyleDefense,
        # "Fighting Style: Dueling": FightingStyleDueling,
        "Fighting Style: Great Weapon Fighting": FightingStyleGreatWeapon,
        # "Fighting Style: Protection": FightingStyleProtection,
        # "Fighting Style: Two-Weapon Fighting": FightingStyleTwoWeapon,
        # "Grappler": Grappler,
        # "Great Weapon Master": GreatWeaponMaster,
        # "Heavily Armored": HeavilyArmored,
        # "Heavy Armor Master": HeavyArmorMaster,
        # "Inspiring Leader": InspiringLeader,
        # "Keen Mind": KeenMind,
        # "Lightly Armored": LightlyArmored,
        # "Mage Slayer": MageSlayer,
        # "Medium Armor Master": MediumArmorMaster,
        # "Mounted Combatant": MountedCombatant,
        # "Observant": Observant,
        # "Polearm Master": PolearmMaster,
        # "Resilient": Resilient,
        # "Ritual Caster": RitualCaster,
        # "Sentinel": Sentinel,
        # "Sharpshooter": Sharpshooter,
        # "Shield Master": ShieldMaster,
        # "Skulker": Skulker,
        # "Speedster": Speedster,
        # "Spell Sniper": SpellSniper,
        # "War Caster": WarCaster,
        # "Weapon Training": WeaponTraining,
    },
    "Spells": {
        "Barkskin": Barkskin,
        "Guidance": Guidance,
    },
}
