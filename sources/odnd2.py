"""
Content from the Dungeons and Dragons OneD&D Expert Classes Unearthed Arcana.
https://media.dndbeyond.com/compendium-images/one-dnd/expert-classes/kpx0MvyfBGHe0XKk/UA2022-Expert-Classes.pdf
"""

from rules import classes, spells
from rules.enums import Skills, SpellLists, SpellSchools


class ThiefRogue(classes.Rogue):
    """
    Thief subclass for Rogue
    UA p. 15
    """

    def __init__(self,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 skill4: Skills
                 ):
        super().__init__(name="Thief Rogue",
                         skill1=skill1,
                         skill2=skill2,
                         skill3=skill3,
                         skill4=skill4)


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
        # "Ability Score Improvement": AbilityScoreImprovement,
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
