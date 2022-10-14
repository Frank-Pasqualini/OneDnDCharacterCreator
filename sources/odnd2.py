"""
Content from the Dungeons and Dragons OneD&D Expert Classes Unearthed Arcana.
https://media.dndbeyond.com/compendium-images/one-dnd/expert-classes/kpx0MvyfBGHe0XKk/UA2022-Expert-Classes.pdf
"""

from rules import abilities, classes, feats, spells
from rules.enums import AbilityNames, SpellLists, SpellSchools


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
                                                     "deals an extra 1d8 damage to the target if it’s missing any of "
                                                     "its Hit Points. You can deal this extra damage only once per "
                                                     "turn."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Hunter's Lore",
                                         description="You can call on the forces of nature to reveal certain "
                                                     "strengths and weaknesses of your prey. While a creature is "
                                                     "marked by your Hunter’s Mark,you know whether that creature has "
                                                     "any Immunities,Resistances, and Vulnerabilities, and if the "
                                                     "creature has any,you know what they are."))

    def _level_up_10(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Multiattack",
                                         description="You now always have Conjure Barrage prepared, and it doesn't "
                                                     "count against the number of Spells you can prepare.\n"
                                                     "You can also cast the Spell with 1st- and 2nd-level Spell "
                                                     "Slots. When you do so,the Spell’s damage is reduced by 1d8 for "
                                                     "each slot level below 3rd.",
                                         feat_spells=[content["Spells"]["Conjure Barrage"]]))

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Superior Hunter's Defense",
                                         description="When you are hit by an Attack Roll,you can use your Reaction to "
                                                     "halve the attack’s damage against yourself,and you can redirect "
                                                     "the other half of the damage to one creature (other than the "
                                                     "attacker) that you can see within 5 feet of yourself."))


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
                                                     "pick a lock or disarm a trap with Thieves’ Tools or to pick a "
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
                                                     "provided you aren’t wearing Medium or Heavy Armor."))

    def _level_up_10(self, feat: feats.Feat):
        if feat.get_level() > 10:
            raise Exception("Invalid feat level. Must be 10 or lower")

        self._features.append(feat)
        self._features.append(feats.Feat(name="Use Magic Device",
                                         description="In your treasure hunting,you have learned how to maximize use "
                                                     "of magic items, granting you the following benefits:\n "
                                                     "Attunement. You can attune to up to four magic items at once.\n"
                                                     "Charges. Whenever you use a magic item property that expends "
                                                     "charges, roll a d6. On a roll of 6, you use the property "
                                                     "without expending the charges.\n "
                                                     "Scrolls. You can use any Spell Scroll that bears a cantrip or a "
                                                     "1st-level Spell. You can also try to use any Spell Scroll that "
                                                     "contains a higher-level Spell, but you must first succeed on an "
                                                     "Intelligence Check (Arcana) with a DC equal to 10 + the Spell’s "
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
                         material_components=True,
                         material_components_list="a handful of bark",
                         concentration=True,
                         duration="1 hour",
                         description="You touch one willing creature to protect it with regenerating bark. Until the "
                                     "Spell ends, the target’s skin assumes a bark-like appearance, and at the start "
                                     "of each of the target’s turns, the target gains a number of Temporary Hit "
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
                                     "Once a creature rolls the die for this Spell,that creature can’t benefit from "
                                     "the Spell again until the creature finishes a Long Rest.")


CONTENT = {
    #  TODO The rest of the subclasses
    "Classes": {
        # "Hunter Ranger": HunterRanger,
        # "Lore Bard": LoreBard,
        "Thief Rogue": ThiefRogue,
    },
    # TODO the feats
    "Feats": {
        "Ability Score Improvement": AbilityScoreImprovement,
        # "Actor": Actor,
        # "Athlete": Athlete,
        # "Charger": Charger,
        # "Crossbow Expert": CrossbowExpert,
        # "Defensive Duelist": DefensiveDuelist,
        # "Dual Wielder": DualWielder,
        # "Durable": Durable,
        # "Elemental Adept": ElementalAdept,
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
        # "Fighting Style: Archery": FightingStyleArchery,
        # "Fighting Style: Defense": FightingStyleDefense,
        # "Fighting Style: Dueling": FightingStyleDueling,
        # "Fighting Style: Great Weapon Fighting": FightingStyleGreatWeapon,
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
