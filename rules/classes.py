"""
A specialization a character can have.
"""
import logging
import math
from abc import ABC, abstractmethod

from rules import bonuses, feats, spells
from rules.common import validate_string
from rules.enums import AbilityNames, ArmorTraining, ClassGroups, Languages, MusicalInstruments, ProficiencyLevels
from rules.enums import Skills, SpellLists, SpellSchools, Tools, WeaponTypes


class CharacterClass(ABC):
    """
    A specialization a character can have.
    """

    _name: str
    _class_group: ClassGroups
    _primary_abilities: list[AbilityNames]
    _features: list[feats.Feat]
    _hit_die: int
    _bonuses: bonuses.Bonuses
    _level: int
    _rolled_hit_dice: list[int]
    _spellcasting_ability: AbilityNames | None

    def __init__(self,
                 name: str,
                 class_group: ClassGroups,
                 primary_abilities: list[AbilityNames],
                 features: list[feats.Feat],
                 hit_die: int,
                 class_bonuses: bonuses.Bonuses,
                 spellcasting_ability: AbilityNames = None):
        if hit_die not in [6, 8, 10, 12]:
            raise Exception("Invalid hit die")

        self._name = validate_string(name)
        self._class_group = class_group
        self._primary_abilities = primary_abilities
        self._features = features
        self._hit_die = hit_die
        self._bonuses = class_bonuses
        self._spellcasting_ability = spellcasting_ability

        self._level = 1
        self._rolled_hit_dice = [hit_die]

    @abstractmethod
    def _level_up_2(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_3(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_4(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_5(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_6(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_7(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_8(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_9(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_10(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_11(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_12(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_13(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_14(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_15(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_16(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_17(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_18(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_19(self, **kwargs):
        pass

    @abstractmethod
    def _level_up_20(self, **kwargs):
        pass

    def _level_up_past_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_bonuses(self) -> bonuses.Bonuses:
        return self._bonuses

    def get_features(self) -> list[feats.Feat]:
        return self._features

    def get_hit_die(self) -> int:
        return self._hit_die

    @abstractmethod
    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        pass

    def get_level(self) -> int:
        return self._level

    def get_rolled_hit_dice(self) -> list[int]:
        return self._rolled_hit_dice

    def get_spellcasting_ability(self) -> AbilityNames | None:
        return self._spellcasting_ability

    @abstractmethod
    def get_spellcasting_class(self) -> str | None:
        pass

    @abstractmethod
    def get_spellcasting_level(self) -> float:
        pass

    def level_up(self, hit_roll: int = -1, **kwargs):
        """
        Level up a class.
        """

        if hit_roll < 1 or hit_roll > self._hit_die:
            if hit_roll != -1:
                logging.warning("Invalid hit roll entered")
            hit_roll = int((self._hit_die + 2) / 2)

        level_up_n = {
            1: self._level_up_2,
            2: self._level_up_3,
            3: self._level_up_4,
            4: self._level_up_5,
            5: self._level_up_6,
            6: self._level_up_7,
            7: self._level_up_8,
            8: self._level_up_9,
            9: self._level_up_10,
            10: self._level_up_11,
            11: self._level_up_12,
            12: self._level_up_13,
            13: self._level_up_14,
            14: self._level_up_15,
            15: self._level_up_16,
            16: self._level_up_17,
            17: self._level_up_18,
            18: self._level_up_19,
            19: self._level_up_20,
        }

        if self._level >= 20:
            self._level_up_past_20(**kwargs)
        else:
            # noinspection PyArgumentList
            level_up_n[self._level](**kwargs)
            self._level += 1
            self._rolled_hit_dice.append(hit_roll)

    def __str__(self):
        return f"{self._name} {self._level}"


class Bard(CharacterClass, ABC):
    """
    The Bard class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 instrument1: MusicalInstruments,
                 instrument2: MusicalInstruments,
                 instrument3: MusicalInstruments):
        if (skill1 == skill2) or (skill1 == skill3) or (skill2 == skill3):
            raise Exception("All 3 skills must be unique")

        if (instrument1 == instrument2) or (instrument1 == instrument3) or (instrument2 == instrument3):
            raise Exception("All 3 instruments must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.EXPERT,
                         primary_abilities=[AbilityNames.CHARISMA],
                         features=[
                             feats.Feat(name="Bardic Inspiration",
                                        description="You can supernaturally inspire others through words, music, "
                                                    "or dance.This inspiration is represented by your Bardic "
                                                    "Inspiration die, which is a d6.\n"
                                                    "Using Bardic Inspiration. You can use your Bardic Inspiration "
                                                    "die in the following ways:\n"
                                                    "Boost a d20 Test. When another creature within 60 feet of you "
                                                    "that you can see or hear fails a d20 Test, you can use your "
                                                    "Reaction to give the creature a Bardic Inspiration die. The "
                                                    "creature rolls that die and adds the number rolled to the d20, "
                                                    "potentially turning the failure into a success.\n"
                                                    "Heal. Immediately after another creature within 60 feet of you "
                                                    "that you can see or hear takes damage, you can use your Reaction "
                                                    "to roll your Bardic Inspiration die and restore a number of Hit "
                                                    "Points to the creature equal to the number rolled.\n"
                                                    "Number of Uses. A Bardic Inspiration die is expended when it's "
                                                    "rolled. You can confer a Bardic Inspiration die a number of "
                                                    "times equal to your Proficiency Bonus,and you regain all "
                                                    "expended uses when you finish a Long Rest.\n"
                                                    "At Higher Levels. Your Bardic Inspiration die changes when you "
                                                    "reach certain levels in this Class,as shown in the Bardic Die "
                                                    "column of the Bard table. The die becomes a d8 at 5th level, "
                                                    "a d10 at 10th level, and a d12 at 15th level."),
                             feats.Feat(name="Spellcasting",
                                        description="Spell Preparation. Any Spell you prepare for this Class must be "
                                                    "an Arcane Spell, and it must be from one of the following "
                                                    "Schools of Magic: Divination, Enchantment, Illusion,"
                                                    "or Transmutation.\n"
                                                    "Whenever you finish a Long Rest, you can practice your bardic "
                                                    "arts and replace any Spell you have prepared for this Class with "
                                                    "another Arcane Spell of the same level, abiding by the school "
                                                    "restriction above.\n"
                                                    "Your spell slots determine the number of different Spells you "
                                                    "can prepare of each level.\n"
                                                    "Spellcasting Ability. Charisma is your Spellcasting Ability for "
                                                    "your Bard Spells.\n"
                                                    "Spellcasting Focus. You can use a Musical Instrument as a "
                                                    "Spellcasting Focus for the Spells you prepare for this Class. "
                                        )
                         ],
                         hit_die=8,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.DEXTERITY: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.CHARISMA: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                                 skill3: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 instrument1: ProficiencyLevels.PROFICIENT,
                                 instrument2: ProficiencyLevels.PROFICIENT,
                                 instrument3: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[ArmorTraining.LIGHT],
                             weapon_types=[WeaponTypes.SIMPLE]
                         ),
                         spellcasting_ability=AbilityNames.CHARISMA)

    def _level_up_2(self,
                    content: dict[str, dict[str, any]],
                    expertise1: Skills,
                    expertise2: Skills):
        self._features.append(feats.Feat(name="Expertise",
                                         description=f"You gain expertise in {expertise1.value} and "
                                                     f"{expertise2.value}.",
                                         feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                                              expertise2: ProficiencyLevels.EXPERT}),
                                         visible=False))
        self._features.append(feats.Feat(name="Song of Restoration",
                                         description="You have learned how to use music, poetry, and dance to heal "
                                                     "wounds and maladies. When you reach certain levels in this "
                                                     "Class, you add a specific Spell to your Songs of Restoration "
                                                     "repertoire, as shown on the Songs of Restoration Repertoire "
                                                     "table. You always have that Spell prepared, and it doesn't "
                                                     "count against the number of Spells you can prepare.",
                                         feat_spells=[
                                             content["Spells"]["Healing Word"](),
                                             content["Spells"]["Lesser Restoration"](
                                             ),
                                             content["Spells"]["Mass Healing Word"](
                                             ),
                                             content["Spells"]["Freedom of Movement"](
                                             ),
                                             content["Spells"]["Greater Restoration"](
                                             )
                                         ]))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Jack of All Trades",
                                         description="You can add half your Proficiency Bonus (round down) to any "
                                                     "Ability Check you make that uses a Skill Proficiency you lack "
                                                     "and that doesn't otherwise use your Proficiency Bonus. For "
                                                     "example, if you make a Strength Check (Athletics) and lack "
                                                     "Athletics Proficiency, you can add half your Proficiency Bonus "
                                                     "to the check.",
                                         feat_bonuses=bonuses.Bonuses(
                                             skills={
                                                 Skills.ACROBATICS: ProficiencyLevels.HALF,
                                                 Skills.ANIMAL_HANDLING: ProficiencyLevels.HALF,
                                                 Skills.ARCANA: ProficiencyLevels.HALF,
                                                 Skills.ATHLETICS: ProficiencyLevels.HALF,
                                                 Skills.DECEPTION: ProficiencyLevels.HALF,
                                                 Skills.HISTORY: ProficiencyLevels.HALF,
                                                 Skills.INSIGHT: ProficiencyLevels.HALF,
                                                 Skills.INTIMIDATION: ProficiencyLevels.HALF,
                                                 Skills.INVESTIGATION: ProficiencyLevels.HALF,
                                                 Skills.MEDICINE: ProficiencyLevels.HALF,
                                                 Skills.NATURE: ProficiencyLevels.HALF,
                                                 Skills.PERCEPTION: ProficiencyLevels.HALF,
                                                 Skills.PERFORMANCE: ProficiencyLevels.HALF,
                                                 Skills.PERSUASION: ProficiencyLevels.HALF,
                                                 Skills.RELIGION: ProficiencyLevels.HALF,
                                                 Skills.SLEIGHT_OF_HAND: ProficiencyLevels.HALF,
                                                 Skills.STEALTH: ProficiencyLevels.HALF,
                                                 Skills.SURVIVAL: ProficiencyLevels.HALF,
                                             }),
                                         visible=False))

    def _level_up_7(self):
        self._features.append(feats.Feat(
            name="Font of Bardic Inspiration",
            description="You now regain all your expended uses of Bardic Inspiration when you finish a Short Rest or "
                        "a Long Rest.\n"
                        "In addition, if a creature rolls your Bardic Inspiration die and gets a 1 (after any rerolls "
                        "you might have), that use of your Bardic Inspiration isn't expended."))

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self, expertise1: Skills, expertise2: Skills):
        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        self._features.append(feats.Feat(
            name="Expertise",
            description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
            feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                 expertise2: ProficiencyLevels.EXPERT}),
            visible=False))

    def _level_up_11(self, spell_list: SpellLists):
        self._features.append(feats.Feat(name="Magical Secrets",
                                         description="You have collected magical knowledge from a wide spectrum of "
                                                     "disciplines. Whenever you prepare Spells for this Class, "
                                                     f"up to two of the Spells you prepare can be from {spell_list} "
                                                     "and from any School of Magic. The prepared Spells otherwise "
                                                     "follow the rules of your Bard Spellcasting feature."))  # TODO

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        pass

    def _level_up_15(self, spell_list: SpellLists):
        self._features.append(feats.Feat(name="Magical Secrets",
                                         description="Your understanding of magic has grown even broader. Whenever "
                                                     "you prepare Spells for this Class, up to two of the Spells you "
                                                     f"prepare can be from {spell_list} and from any School of Magic. "
                                                     "The prepared Spells otherwise follow the rules of your Bard "
                                                     "Spellcasting feature."))  # TODO

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        pass

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Superior Bardic Inspiration",
                                         description="When you roll Initiative, you regain two expended uses of your "
                                                     "Bardic Inspiration."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        return [spell() for spell in content["Spells"].values() if
                spell().get_level() in range(0, math.ceil(self._level / 2) + 1) and
                SpellLists.ARCANE in spell().get_spell_lists() and
                spell().get_school() in [
                    SpellSchools.DIVINATION,
                    SpellSchools.ENCHANTMENT,
                    SpellSchools.ILLUSION,
                    SpellSchools.TRANSMUTATION]
                ]

    def get_spellcasting_class(self) -> str | None:
        return "Bard"

    def get_spellcasting_level(self) -> float:
        return self._level


class Cleric(CharacterClass, ABC):
    """
    The Cleric class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills):
        allowable_skills = [Skills.HISTORY, Skills.INSIGHT,
                            Skills.MEDICINE, Skills.PERSUASION, Skills.RELIGION]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills):
            raise Exception(
                "All skills must be in the approved skill list")

        if skill1 == skill2:
            raise Exception("Both skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.PRIEST,
                         primary_abilities=[AbilityNames.WISDOM],
                         features=[
                             feats.Feat(name="Channel Divinity",
                                        description="You gain the ability to channel divine energy directly from the "
                                                    "Outer Planes, using that energy to fuel magical effects. You "
                                                    "start with two such effects: Divine Spark and Turn Undead, "
                                                    "each of which is described below. Each time you use your Channel "
                                                    "Divinity, you choose which effect to create, and you gain "
                                                    "additional effect options at higher levels in this Class.\n"
                                                    "You can use your Channel Divinity a number of times equal to "
                                                    "your Proficiency Bonus, and you regain all expended uses when "
                                                    "you finish a Long Rest.\n"
                                                    "Some Channel Divinity effects require Saving Throws. When you "
                                                    "use such an effect from this Class, the DC equals the Spell Save "
                                                    "DC from this Class's Spellcasting feature.\n"
                                                    "Divine Spark. As a Magic Action, you point your Holy Symbol at "
                                                    "another creature you can see within 30 feet of yourself and "
                                                    "focus divine energy at them. Roll a number of d8s equal to your "
                                                    "Proficiency Bonus and add the rolls together. You either restore "
                                                    "Hit Points to the creature equal to that total or force the "
                                                    "creature to make a Constitution Saving Throw. On a failed save, "
                                                    "the creature takes Radiant Damage equal to the total, "
                                                    "and on a successful save, the creature takes half as much damage "
                                                    "(rounded down).\n"
                                                    "Turn Undead. As a Magic Action, you present your Holy Symbol and "
                                                    "speak a prayer censuring Undead creatures. Each Undead within 30 "
                                                    "feet of you must make a Wisdom Saving Throw. If the creature "
                                                    "fails its Saving Throw, it is Dazed for 1 minute or until it "
                                                    "takes any damage or you are Incapacitated or die. While Dazed in "
                                                    "this way, the only Action the creature can take is the Dash "
                                                    "Action, and if it Moves, it must end that Move farther from you "
                                                    "than where it started."),
                             feats.Feat(name="Spellcasting",
                                        description="Spell Preparation. Any Spell you prepare for this Class must be "
                                                    "a Divine Spell.\n"
                                                    "Whenever you finish a Long Rest, you can pray or meditate and "
                                                    "replace any Spell you have prepared for this Class with "
                                                    "another Divine Spell of the same level.\n"
                                                    "Your spell slots determine the number of different Spells you "
                                                    "can prepare of each level.\n"
                                                    "Spellcasting Ability. Wisdom is your Spellcasting Ability for "
                                                    "your Cleric Spells.\n"
                                                    "Spellcasting Focus. You can use a Holy Symbol as a "
                                                    "Spellcasting Focus for the Spells you prepare for this Class. "
                                        )
                         ],
                         hit_die=8,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.WISDOM: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.CHARISMA: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[
                                 ArmorTraining.LIGHT, ArmorTraining.MEDIUM, ArmorTraining.SHIELD],
                             weapon_types=[WeaponTypes.SIMPLE]
                         ),
                         spellcasting_ability=AbilityNames.WISDOM)

    def _level_up_2(self, holy_order: feats.HolyOrder):
        self._features.append(holy_order)

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Smite Undead",
                                         description="You can cause your Turn Undead feature to smite the undying; "
                                                     "whenever you use Turn Undead, you can roll a number of d8s "
                                                     "equal to your Proficiency Bonus and add the rolls together. "
                                                     "Each Undead that fails its Saving Throw against that use of "
                                                     "Turn Undead takes Radiant Damage equal to the roll's total."))

    def _level_up_7(self):
        self._features.append(feats.Feat(
            name="Blessed Strikes",
            description="Divine power infuses you in battle. When a creature takes damage from one of your 0-level "
                        "Spells or your attacks with Weapons, you can also deal 1d8 Radiant Damage to that creature. "
                        "Once you deal this damage, you can't use this feature again until the start of your next "
                        "turn."))

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self, holy_order: feats.HolyOrder):
        self._features.append(holy_order)

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Divine Intervention",
                                         description="You can call on your deity or pantheon to intervene on your "
                                                     "behalf when your need is great. As an Action, describe the "
                                                     "assistance you seek, and roll percentile dice. If you roll a "
                                                     "number equal to or lower than your Cleric level, the divine "
                                                     "power intervenes. The DM chooses the nature of the "
                                                     "intervention; the effect of any Divine Spell is appropriate. If "
                                                     "the intervention occurs, you can't use this feature again for "
                                                     "2d6 days. Otherwise, you can use it again after you finish a "
                                                     "Long Rest."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        pass

    def _level_up_15(self):
        pass

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        pass

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Greater Divine Intervention",
                                         description="When you use your Divine Intervention feature, it succeeds "
                                                     "automatically-no roll required-and you can use it again after "
                                                     "2d4 days."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        return [spell() for spell in content["Spells"].values() if
                spell().get_level() in range(0, math.ceil(self._level / 2) + 1) and
                SpellLists.DIVINE in spell().get_spell_lists()]

    def get_spellcasting_class(self) -> str | None:
        return "Cleric"

    def get_spellcasting_level(self) -> float:
        return self._level


class Fighter(CharacterClass, ABC):
    """
    The Fighter class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 fighting_style: feats.FightingStyle,
                 ):
        allowable_skills = [Skills.ACROBATICS, Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.HISTORY, Skills.INSIGHT,
                            Skills.INTIMIDATION, Skills.PERCEPTION, Skills.SURVIVAL]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills):
            raise Exception("All skills must be in the approved skill list")

        if skill1 == skill2:
            raise Exception("All skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.WARRIOR,
                         primary_abilities=[AbilityNames.STRENGTH],
                         features=[
                             fighting_style,
                             feats.Feat(name="Second Wind",
                                        description="You have a limited well of stamina that you can draw on to "
                                                    "protect yourself from harm. On your turn, you can use a bonus "
                                                    "action to regain hit points equal to 1d10 + your fighter level. "
                                                    "Once you use this feature, you must finish a short or long rest "
                                                    "before you can use it again.")
                         ],
                         hit_die=10,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.STRENGTH: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.CONSTITUTION: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[ArmorTraining.LIGHT, ArmorTraining.MEDIUM, ArmorTraining.HEAVY,
                                             ArmorTraining.SHIELD],
                             weapon_types=[WeaponTypes.SIMPLE,
                                           WeaponTypes.MARTIAL]
                         ))

    def _level_up_2(self):
        self._features.append(feats.Feat(name="Action Surge",
                                         description="You can push yourself beyond your normal limits for a moment. "
                                                     "On your turn, you can take one additional action on top of your "
                                                     "regular action and a possible bonus action. Once you use this "
                                                     "feature, you must finish a short or long rest before you can "
                                                     "use it again.\n"
                                                     "Starting at 17th level, you can use it twice before a rest, "
                                                     "but only once on the same turn. "))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Extra Attack",
                                         description="You can attack twice, instead of once, whenever you take the "
                                                     "Attack action on your turn.\n"
                                                     "The number of attacks increases to three when you reach 11th "
                                                     "level in this class and to four when you reach 20th level in "
                                                     "this class. "))

    def _level_up_6(self, feat: feats.Feat):
        if feat.get_level() > 6:
            raise Exception("Invalid feat level. Must be 6 or lower")

        self._features.append(feat)

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self):
        self._features.append(feats.Feat(name="Indomitable",
                                         description="You can reroll a saving throw that you fail. If you do so, "
                                                     "you must use the new roll, and you can't use this feature again "
                                                     "until you finish a long rest.\n"
                                                     "You can use this feature twice between long rests starting at "
                                                     "13th level and three times between long rests starting at 17th "
                                                     "level."))

    def _level_up_11(self):
        pass

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        pass

    def _level_up_14(self, feat: feats.Feat):
        if feat.get_level() > 14:
            raise Exception("Invalid feat level. Must be 14 or lower")

        self._features.append(feat)

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        pass

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        pass

    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        return []

    def get_spellcasting_class(self) -> str | None:
        return None

    def get_spellcasting_level(self) -> float:
        return 0


class Paladin(CharacterClass, ABC):
    """
    The Paladin class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills):
        allowable_skills = [Skills.ATHLETICS, Skills.INSIGHT, Skills.INTIMIDATION, Skills.MEDICINE, Skills.PERSUASION,
                            Skills.RELIGION]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills):
            raise Exception(
                "All skills must be in the approved skill list")

        if skill1 == skill2:
            raise Exception("All skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.PRIEST,
                         primary_abilities=[
                             AbilityNames.STRENGTH, AbilityNames.CHARISMA],
                         features=[
                             feats.Feat(name="Divine Sense",
                                        description="The presence of strong evil registers on your senses like a "
                                                    "noxious odor, and powerful good rings like heavenly music in "
                                                    "your ears. As an action, you can open your awareness to detect "
                                                    "such forces. Until the end of your next turn, you know the "
                                                    "location of any celestial, fiend, or undead within 60 feet of "
                                                    "you that is not behind total cover. You know the type ("
                                                    "celestial, fiend, or undead) of any being whose presence you "
                                                    "sense, but not its identity (the vampire Count Strahd von "
                                                    "Zarovich, for instance). Within the same radius, you also detect "
                                                    "the presence of any place or object that has been consecrated or "
                                                    "desecrated, as with the hallow spell.\n"
                                                    "You can use this feature a number of times equal to 1 + your "
                                                    "Charisma modifier. When you finish a long rest, you regain all "
                                                    "expended uses."),
                             feats.Feat(name="Lay On Hands",
                                        description="Your blessed touch can heal wounds. You have a pool of healing "
                                                    "power that replenishes when you take a long rest. With that "
                                                    "pool, you can restore a total number of hit points equal to your "
                                                    "paladin level × 5.\n"
                                                    "As an action, you can touch a creature and draw power from the "
                                                    "pool to restore a number of hit points to that creature, "
                                                    "up to the maximum amount remaining in your pool.\n"
                                                    "Alternatively, you can expend 5 hit points from your pool of "
                                                    "healing to cure the target of one disease or neutralize one "
                                                    "poison affecting it. You can cure multiple diseases and "
                                                    "neutralize multiple poisons with a single use of Lay on Hands, "
                                                    "expending hit points separately for each one.\n"
                                                    "This feature has no effect on undead and constructs.")
                         ],
                         hit_die=10,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.WISDOM: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.CHARISMA: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[
                                 ArmorTraining.LIGHT, ArmorTraining.MEDIUM, ArmorTraining.HEAVY, ArmorTraining.SHIELD],
                             weapon_types=[WeaponTypes.SIMPLE,
                                           WeaponTypes.MARTIAL]
                         ),
                         spellcasting_ability=AbilityNames.CHARISMA)

    def _level_up_2(self, fighting_style: feats.FightingStyle):
        if fighting_style.get_level() > 2:
            raise Exception("Invalid fighting style level. Must be 2 or lower")

        self._features.append(fighting_style)
        self._features.append(feats.Feat(name="Spellcasting",
                                         description="Spell Preparation. You prepare the list of paladin spells that "
                                                     "are available for you to cast, choosing from the paladin spell "
                                                     "list. When you do so, choose a number of paladin spells equal "
                                                     "to your Charisma modifier + half your paladin level, "
                                                     "rounded down (minimum of one spell). You can change your list "
                                                     "of prepared spells when you finish a long rest. Preparing a new "
                                                     "list of paladin spells requires time spent in prayer and "
                                                     "meditation: at least 1 minute per spell level for each spell on "
                                                     "your list.\n"
                                                     "Your spell slots determine the number of different Spells you "
                                                     "can prepare of each level.\n"
                                                     "Spellcasting Ability. Charisma is your Spellcasting Ability for "
                                                     "your Paladin Spells.\n"
                                                     "Spellcasting Focus. You can use a holy symbol as a "
                                                     "Spellcasting Focus for your paladin spells."))
        self._features.append(feats.Feat(name="Divine Smite",
                                         description="When you hit a creature with a melee weapon attack, you can "
                                                     "expend one spell slot to deal radiant damage to the target, "
                                                     "in addition to the weapon's damage. The extra damage is 2d8 for "
                                                     "a 1st-level spell slot, plus 1d8 for each spell level higher "
                                                     "than 1st, to a maximum of 5d8. The damage increases by 1d8 if "
                                                     "the target is an undead or a fiend."))

    def _level_up_3(self, content: dict[str, dict[str, any]]):
        del content
        self._features.append(feats.Feat(name="Divine Health",
                                         description="The divine magic flowing through you makes you immune to "
                                                     "disease."))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Extra Attack",
                                         description="You can attack twice, instead of once, whenever you take the "
                                                     "Attack Action on your turn."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Aura of Protection",
                                         description="Whenever you or a friendly creature within 10 feet of you must "
                                                     "make a saving throw, the creature gains a bonus to the saving "
                                                     "throw equal to your Charisma modifier (with a minimum bonus of "
                                                     "+1). You must be conscious to grant this bonus.\n"
                                                     "At 18th level, the range of this aura increases to 30 feet."))
        # TODO Implement Saving throw increase on self

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self):
        pass

    def _level_up_10(self):
        self._features.append(feats.Feat(name="Aura of Courage",
                                         description="You and friendly creatures within 10 feet of you can't be"
                                                     "frightened while you are conscious.\n"
                                                     "At 18th level, the range of this aura increases to 30 feet."))

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Improved Divine Smite",
                                         description="You are so suffused with righteous might that all your melee "
                                                     "weapon strikes carry divine power with them. Whenever you hit a "
                                                     "creature with a melee weapon, the creature takes an extra 1d8 "
                                                     "radiant damage. If you also use your Divine Smite with an "
                                                     "attack, you add this damage to the extra damage of your Divine "
                                                     "Smite."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        pass

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Cleansing Touch",
                                         description="You can use your action to end one spell on yourself or on one "
                                                     "willing creature that you touch.\n"
                                                     "You can use this feature a number of times equal to your "
                                                     "Charisma modifier (a minimum of once). You regain expended uses "
                                                     "when you finish a long rest."))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        pass

    def _level_up_18(self):
        pass

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        known_spells = []

        if self._level >= 2:
            known_spells += [
                content["Spells"]["Bless"](),
                content["Spells"].get(
                    "Ceremony", content["Spells"]["Bless"])(),
                content["Spells"]["Command"](),
                content["Spells"].get(
                    "Compelled Duel", content["Spells"]["Bless"])(),
                content["Spells"]["Cure Wounds"](),
                content["Spells"]["Detect Evil and Good"](),
                content["Spells"]["Detect Magic"](),
                content["Spells"]["Detect Poison and Disease"](),
                content["Spells"]["Divine Favor"](),
                content["Spells"]["Heroism"](),
                content["Spells"]["Protection from Evil and Good"](),
                content["Spells"]["Purify Food and Drink"](),
                content["Spells"].get(
                    "Searing Smite", content["Spells"]["Bless"])(),
                content["Spells"]["Shield of Faith"](),
                content["Spells"].get("Thunderous Smite",
                                      content["Spells"]["Bless"])(),
                content["Spells"].get(
                    "Wrathful Smite", content["Spells"]["Bless"])(),
            ]

        if self._level >= 5:
            known_spells += [
                content["Spells"]["Aid"](),
                content["Spells"]["Branding Smite"](),
                content["Spells"]["Find Steed"](),
                content["Spells"].get(
                    "Gentle Repose", content["Spells"]["Bless"])(),
                content["Spells"]["Lesser Restoration"](),
                content["Spells"]["Locate Object"](),
                content["Spells"]["Magic Weapon"](),
                content["Spells"].get(
                    "Prayer of Healing", content["Spells"]["Bless"])(),
                content["Spells"]["Protection from Poison"](),
                content["Spells"].get(
                    "Warding Bond", content["Spells"]["Bless"])(),
                content["Spells"]["Zone of Truth"](),
            ]

        if self._level >= 9:
            known_spells += [
                content["Spells"].get("Aura of Vitality",
                                      content["Spells"]["Bless"])(),
                content["Spells"].get(
                    "Blinding Smite", content["Spells"]["Bless"])(),
                content["Spells"]["Create Food and Water"](),
                content["Spells"].get(
                    "Crusader's Mantle", content["Spells"]["Bless"])(),
                content["Spells"]["Daylight"](),
                content["Spells"]["Dispel Magic"](),
                content["Spells"].get("Elemental Weapon",
                                      content["Spells"]["Bless"])(),
                content["Spells"]["Magic Circle"](),
                content["Spells"]["Remove Curse"](),
                content["Spells"]["Revivify"](),
                content["Spells"].get(
                    "Spirit Shroud", content["Spells"]["Bless"])(),
            ]

        if self._level >= 13:
            known_spells += [
                content["Spells"].get(
                    "Aura of Life", content["Spells"]["Bless"])(),
                content["Spells"].get(
                    "Aura of Purity", content["Spells"]["Bless"])(),
                content["Spells"]["Banishment"](),
                content["Spells"]["Death Ward"](),
                content["Spells"].get(
                    "Find Greater Steed", content["Spells"]["Bless"])(),
                content["Spells"]["Locate Creature"](),
                content["Spells"].get("Staggering Smite",
                                      content["Spells"]["Bless"])(),
            ]

        if self._level >= 17:
            known_spells += [
                content["Spells"].get(
                    "Banishing Smite", content["Spells"]["Bless"])(),
                content["Spells"].get(
                    "Circle of Power", content["Spells"]["Bless"])(),
                content["Spells"].get("Destructive Wave",
                                      content["Spells"]["Bless"])(),
                content["Spells"]["Dispel Evil and Good"](),
                content["Spells"]["Geas"](),
                content["Spells"].get(
                    "Holy Weapon", content["Spells"]["Bless"])(),
                content["Spells"]["Raise Dead"](),
                content["Spells"].get("Summon Celestial",
                                      content["Spells"]["Bless"])(),
            ]

        return known_spells

    def get_spellcasting_class(self) -> str | None:
        return "Paladin"

    def get_spellcasting_level(self) -> float:
        return self._level / 2


class Ranger(CharacterClass, ABC):
    """
    The Rogue class.
    """

    def __init__(self,
                 content: dict[str, dict[str, any]],
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 expertise1: Skills,
                 expertise2: Skills):
        allowable_skills = [Skills.ANIMAL_HANDLING, Skills.ATHLETICS, Skills.INSIGHT, Skills.INVESTIGATION,
                            Skills.NATURE, Skills.PERCEPTION, Skills.STEALTH, Skills.SURVIVAL]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills) or (skill3 not in allowable_skills):
            raise Exception(
                "All 3 skills must be in the approved skill list")

        if (skill1 == skill2) or (skill1 == skill3) or (skill2 == skill3):
            raise Exception("All 3 skills must be unique")

        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.EXPERT,
                         primary_abilities=[
                             AbilityNames.DEXTERITY, AbilityNames.WISDOM],
                         features=[
                             feats.Feat(name="Expertise",
                                        description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
                                        feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                                             expertise2: ProficiencyLevels.EXPERT}),
                                        visible=False),
                             feats.Feat(name="Favored Enemy",
                                        description="You are adept at focusing your ire on a single foe. You always "
                                                    "have the Hunter's Mark Spell prepared, and it doesn't count "
                                                    "against the number of Spells you can prepare. Moreover, "
                                                    "you don't have to concentrate on the Spell once you cast it; it "
                                                    "lasts for its full duration, until you end it as a Bonus Action, "
                                                    "or until you are Incapacitated.",
                                        feat_spells=[
                                            content["Spells"]["Hunter's Mark"]()],
                                        spellcasting_ability=AbilityNames.WISDOM),
                             feats.Feat(name="Spellcasting",
                                        description="Spell Preparation. Any Spell you prepare for this Class must be "
                                                    "a Primal Spell, and it can be from any School of Magic except "
                                                    "Evocation.\n"
                                                    "Whenever you finish a Long Rest, you can commune with nature and "
                                                    "replace any Spell you have prepared for this Class with another "
                                                    "Primal Spell of the same level that isn't an Evocation.\n"
                                                    "Your spell slots determine the number of different Spells you "
                                                    "can prepare of each level.\n"
                                                    "Spellcasting Ability. Wisdom is your Spellcasting Ability for "
                                                    "your Ranger Spells.\n"
                                                    "Spellcasting Focus. You can use a Druidic Focus as a "
                                                    "Spellcasting Focus for the Spells you prepare for this Class.")
                         ],
                         hit_die=10,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.STRENGTH: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.DEXTERITY: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                                 skill3: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[
                                 ArmorTraining.LIGHT, ArmorTraining.MEDIUM, ArmorTraining.SHIELD],
                             weapon_types=[WeaponTypes.SIMPLE,
                                           WeaponTypes.MARTIAL]
                         ),
                         spellcasting_ability=AbilityNames.WISDOM)

    def _level_up_2(self, fighting_style: feats.FightingStyle):
        if fighting_style.get_level() > 2:
            raise Exception("Invalid fighting style level. Must be 2 or lower")

        self._features.append(fighting_style)

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Extra Attack",
                                         description="You can attack twice, instead of once, whenever you take the "
                                                     "Attack Action on your turn."))

    def _level_up_7(self):
        self._features.append(feats.Feat(
            name="Roving",
            description="Your Speed increases by 10 feet while you aren't wearing Heavy Armor. You also have a Climb "
                        "Speed and a Swim Speed equal to your Speed."))  # TODO Implement Speed increases

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self, expertise1: Skills, expertise2: Skills):
        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        self._features.append(feats.Feat(
            name="Expertise",
            description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
            feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                 expertise2: ProficiencyLevels.EXPERT}),
            visible=False))

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Tireless",
                                         description="Primal forces now help fuel you on your journeys,granting you "
                                                     "the following benefits:\n"
                                                     "Temporary Hit Points. Whenever you finish a Short Rest or a "
                                                     "Long Rest, you can give yourself a number of Temporary Hit "
                                                     "Points equal to 1d8 plus your Proficiency Bonus.\n"
                                                     "Decrease Exhaustion. If you are Exhausted when you finish a "
                                                     "Short Rest, your level of exhaustion decreases by 1."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        self._features.append(feats.Feat(name="Nature's Veil",
                                         description="You invoke spirits of nature to magically hide yourself from "
                                                     "view. As a Bonus Action, you can expend a Spell Slot and become "
                                                     "Invisible until the end of your next turn."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Feral Senses",
                                         description="Your connection to the forces of nature grants you Blindsight "
                                                     "with a range of 30 feet."))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        pass

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Foe Slayer",
                                         description="Your Hunter's Mark now deals an extra 1d10 damage to its "
                                                     "target, rather than an extra 1d6."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        return [spell() for spell in content["Spells"].values() if
                spell().get_level() in range(0, math.ceil(self._level / 4) + 1) and
                SpellLists.PRIMAL in spell().get_spell_lists() and
                spell().get_school() != SpellSchools.EVOCATION]

    def get_spellcasting_class(self) -> str | None:
        return "Ranger"

    def get_spellcasting_level(self) -> float:
        return self._level / 2


class Rogue(CharacterClass, ABC):
    """
    The Rogue class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills,
                 skill3: Skills,
                 skill4: Skills,
                 expertise1: Skills,
                 expertise2: Skills,
                 language: Languages):
        allowable_skills = [Skills.ACROBATICS, Skills.ATHLETICS, Skills.DECEPTION, Skills.INSIGHT, Skills.INTIMIDATION,
                            Skills.INVESTIGATION, Skills.PERCEPTION, Skills.PERSUASION, Skills.SLEIGHT_OF_HAND,
                            Skills.STEALTH]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills) or (skill3 not in allowable_skills) or (
                skill4 not in allowable_skills):
            raise Exception(
                "All 4 skills must be in the approved skill list")

        if (skill1 == skill2) or (skill1 == skill3) or (skill1 == skill4) or (skill2 == skill3) or (
                skill2 == skill4) or (skill3 == skill4):
            raise Exception("All 4 skills must be unique")

        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.EXPERT,
                         primary_abilities=[AbilityNames.DEXTERITY],
                         features=[
                             feats.Feat(name="Expertise",
                                        description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
                                        feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                                             expertise2: ProficiencyLevels.EXPERT}),
                                        visible=False),
                             feats.Feat(name="Sneak Attack",
                                        description="You know how to turn a subtle attack into a deadly one. Once on "
                                                    "each of your turns when you take the Attack Action, you can deal "
                                                    "extra damage to one creature you hit with an Attack Roll if "
                                                    "you're attacking with a Finesse Weapon or a Ranged Weapon and if "
                                                    "at least one of the following requirements is met:\n"
                                                    "Advantage. You have Advantage on the Attack Roll.\n"
                                                    "Ally Adjacent to Target. At least one of your allies is within 5 "
                                                    "feet of the target, the ally isn't Incapacitated, "
                                                    "and you don't have Disadvantage on the Attack Roll.\n"
                                                    "To determine the extra damage, roll a number of d6s equal to "
                                                    "half your Rogue level(round up), and add the dice together. The "
                                                    "extra damage's type is the same as the weapon's Damage Type."),
                             feats.Feat(name="Thieves' Cant",
                                        description="You picked up various languages in the communities where you "
                                                    "plied your roguish talents. You know Thieves' Cant and "
                                                    f"{language.value}.",
                                        feat_bonuses=bonuses.Bonuses(
                                            languages=[Languages.THIEVES_CANT, language]),
                                        visible=False)
                         ],
                         hit_die=8,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.DEXTERITY: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.INTELLIGENCE: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                                 skill3: ProficiencyLevels.PROFICIENT,
                                 skill4: ProficiencyLevels.PROFICIENT
                             },
                             tools={
                                 Tools.THIEVES_TOOLS: ProficiencyLevels.PROFICIENT
                             },
                             armor_training=[ArmorTraining.LIGHT],
                             weapon_types=[WeaponTypes.SIMPLE,
                                           WeaponTypes.MARTIAL_FINESSE]
                         ))

    def _level_up_2(self):
        self._features.append(feats.Feat(name="Cunning Action",
                                         description="Your quick thinking and agility allow you to move and act "
                                                     "quickly. On your turn, you can take one of the following "
                                                     "Actions as a Bonus Action: Dash, Disengage, or Hide."))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Uncanny Dodge",
                                         description="When an attacker that you can see hits you with an Attack Roll, "
                                                     "you can use your Reaction to halve the attack's damage against "
                                                     "you (round down)."))

    def _level_up_7(self, expertise1: Skills, expertise2: Skills):
        if expertise1 == expertise2:
            raise Exception("Expertise skills must be unique")

        self._features.append(feats.Feat(
            name="Expertise",
            description=f"You gain expertise in {expertise1.value} and {expertise2.value}.",
            feat_bonuses=bonuses.Bonuses(skills={expertise1: ProficiencyLevels.EXPERT,
                                                 expertise2: ProficiencyLevels.EXPERT}),
            visible=False))

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self):
        self._features.append(feats.Feat(name="Evasion",
                                         description="You can nimbly dodge out of the way of certain dangers. When "
                                                     "you are subjected to an effect that allows you to make a "
                                                     "Dexterity Saving Throw to take only half damage, you instead "
                                                     "take no damage if you succeed on the Saving Throw and only half "
                                                     "damage if you fail. You can't use this feature if you're "
                                                     "Incapacitated."))

    def _level_up_10(self, feat: feats.Feat):
        if feat.get_level() > 10:
            raise Exception("Invalid feat level. Must be 10 or lower")

        self._features.append(feat)

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Reliable Talent",
                                         description="You have refined your talents until they approach perfection. "
                                                     "Whenever you make an Ability Check that uses one of your Skill "
                                                     "or Tool Proficiencies,you can treat a d20 roll of 9 or lower as "
                                                     "a 10."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        self._features.append(feats.Feat(name="Subtle Strikes",
                                         description="When you attack, you know how to exploit a target's "
                                                     "distraction. You have Advantage on any Attack Roll that targets "
                                                     "a creature that is within 5 feet of at least one of your allies "
                                                     "who isn't Incapacitated."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Slippery Mind",
                                         description="Your cunning mind is exceptionally difficult to control. You "
                                                     "gain Proficiency in Wisdom and Charisma Saving Throws.",
                                         feat_bonuses=bonuses.Bonuses(
                                             saving_throws={AbilityNames.WISDOM: ProficiencyLevels.PROFICIENT,
                                                            AbilityNames.CHARISMA: ProficiencyLevels.PROFICIENT}),
                                         visible=False))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        self._features.append(feats.Feat(name="Elusive",
                                         description="You are so evasive that attackers rarely gain the upper hand "
                                                     "against you. No Attack Roll has Advantage against you while you "
                                                     "aren't Incapacitated."))

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Stroke of Luck",
                                         description="You have an uncanny knack for succeeding when you need to. If "
                                                     "you fail a d20 Test,you can turn the roll into a 20.\n"
                                                     "Once you use this feature, you can't use it again until you "
                                                     "finish a Short Rest or a Long Rest."))

    def _level_up_19(self, feat: feats.Feat):
        if feat.get_level() > 19:
            raise Exception("Invalid feat level. Must be 19 or lower")

        self._features.append(feat)

    def _level_up_20(self, feat: feats.Feat):
        if feat.get_level() > 20:
            raise Exception("Invalid feat level. Must be 20 or lower")

        self._features.append(feat)

    def get_known_spells(self, content: dict[str, dict[str, any]]) -> list[spells.Spell]:
        return []

    def get_spellcasting_class(self) -> str | None:
        return None

    def get_spellcasting_level(self) -> float:
        return 0
