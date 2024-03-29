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


class Druid(CharacterClass, ABC):
    """
    The Druid class.
    """

    def __init__(self,
                 name: str,
                 skill1: Skills,
                 skill2: Skills):
        allowable_skills = [Skills.ARCANA, Skills.ANIMAL_HANDLING, Skills.INSIGHT, Skills.MEDICINE, Skills.NATURE,
                            Skills.PERCEPTION, Skills.RELIGION, Skills.SURVIVAL]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills):
            raise Exception(
                "All skills must be in the approved skill list")

        if skill1 == skill2:
            raise Exception("All skills must be unique")

        super().__init__(name=name,
                         class_group=ClassGroups.PRIEST,
                         primary_abilities=[AbilityNames.WISDOM],
                         features=[
                             feats.Feat(name="Channel Nature",
                                        description="The magic of nature infuses you. Tapping into that power, "
                                                    "you can create various magical effects. You start with one such "
                                                    "effect: Wild Shape, which is described below. Other Druid "
                                                    "features give additional Channel Nature effect options. Each "
                                                    "time you use this Channel Nature, you choose which effect to "
                                                    "create from among those you have from this class.\n"
                                                    "You can use Channel Nature twice. You regain one expended use "
                                                    "when you finish a Short Rest, and you regain all expended uses "
                                                    "when you finish a Long Rest. You gain additional uses when you "
                                                    "reach certain Druid levels, as shown in the Channel Nature "
                                                    "column of the Druid table.\n"
                                                    "If a Channel Nature effect requires a saving throw, the DC "
                                                    "equals the Spell Save DC from this class's Spellcasting feature.\n"
                                                    "Wild Shape. As a Magic action, you transform into a form that "
                                                    "you have learned for this feature. You start knowing one form, "
                                                    "Animal of the Land, which is detailed in the 'Wild Shapes' "
                                                    "section later in this class's description. You stay in that form "
                                                    "for a number of hours equal to half your Druid level or until "
                                                    "you use Wild Shape again, have the Incapacitated condition, "
                                                    "or die. You can also end Wild Shape early as a Bonus Action.\n"
                                                    "While in a form, its game statistics replace yours, and your "
                                                    "ability to handle objects is determined by the form's limbs, "
                                                    "rather than your own. You retain your personality, memories, "
                                                    "ability to speak, and Wild Shape. You lose access to all your "
                                                    "other features, such as the ability to cast spells (you can "
                                                    "continue to concentrate on  one).\n"
                                                    "When you transform, you choose whether  your equipment falls to "
                                                    "the ground in your space  or merges into your new form. "
                                                    "Equipment that  merges with the form has no effect until you  "
                                                    "leave the form."),
                             feats.Feat(name="Druidic",
                                        description="You know Druidic, the secret language of Druids. You can speak "
                                                    "the language and use it to leave hidden messages.\n"
                                                    "You and others who know this language automatically spot such a "
                                                    "message. Others spot the message's presence with a successful DC "
                                                    "15 Intelligence (Investigation) check but can't decipher it "
                                                    "without magic.",
                                        feat_bonuses=bonuses.Bonuses(languages=[Languages.DRUIDIC])),
                             feats.Feat(name="Spellcasting",
                                        description="Spell Preparation. Any Spell you prepare for this Class must be "
                                                    "a Primal Spell.\n"
                                                    "Whenever you finish a Long Rest, you can meditate and replace any "
                                                    "Spell you have prepared for this Class with another Primal Spell "
                                                    "of the same level.\n"
                                                    "Your spell slots determine the number of different Spells you "
                                                    "can prepare of each level.\n"
                                                    "Spellcasting Ability. Wisdom is your Spellcasting Ability for "
                                                    "your Druid Spells.\n"
                                                    "Spellcasting Focus. You can use a Druidic Focus as a "
                                                    "Spellcasting Focus for the Spells you prepare for this Class.")
                         ],
                         hit_die=8,
                         class_bonuses=bonuses.Bonuses(
                             saving_throws={
                                 AbilityNames.INTELLIGENCE: ProficiencyLevels.PROFICIENT,
                                 AbilityNames.WISDOM: ProficiencyLevels.PROFICIENT,
                             },
                             skills={
                                 skill1: ProficiencyLevels.PROFICIENT,
                                 skill2: ProficiencyLevels.PROFICIENT,
                             },
                             tools={
                                 Tools.HERBALISM_KIT: ProficiencyLevels.PROFICIENT,
                             },
                             armor_training=[
                                 ArmorTraining.LIGHT, ArmorTraining.SHIELD],
                             weapon_types=[WeaponTypes.SIMPLE],
                         ),
                         spellcasting_ability=AbilityNames.WISDOM)

    def _level_up_2(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Nature's Aid",
                                         description="You learn two more ways to use your Channel Nature - Healing "
                                                     "Blossoms and Wild Companion - each of which is described below.\n"
                                                     "Healing Blossoms. As a Magic action, you channel healing energy "
                                                     "that appears as blooming flowers. Choose a point within 30 feet "
                                                     "of yourself, and spectral flowers appear for a moment in a "
                                                     "10-foot-radius sphere centered on that point. Then roll a "
                                                     "number of d4s equal to your Wisdom modifier (minimum of one "
                                                     "die), and add the dice together. The total is the number of Hit "
                                                     "Points you can distribute to creatures in that sphere. You "
                                                     "decide the number of Hit Points that are restored to each of "
                                                     "those creatures, deducting the healing from the total.\n"
                                                     "Wild Companion. You can summon a nature spirit that assumes an "
                                                     "animal form to aid you. As a Magic action, you can expend a use "
                                                     "of your Channel Nature and cast the Find Familiar spell without "
                                                     "material components.\n"
                                                     "When you cast the spell in this way, the familiar is a Fey, "
                                                     "and it disappears when you finish a Long Rest.",
                                         feat_spells=[
                                             content["Spells"]["Find Familiar"]()],
                                         spellcasting_ability=AbilityNames.WISDOM))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self):
        self._features.append(feats.Feat(name="Might of the Land",
                                         description="Your connection to the land deepens, empowering the Animal of "
                                                     "the Land form of your Wild Shape; you unlock that form's Climb "
                                                     "Speed and Multiattack."))

    def _level_up_7(self):
        self._features.append(feats.Feat(name="Aquatic Form",
                                         description="You learn a new form for your Wild Shape: Animal of the Sea."))

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self):
        self._features.append(feats.Feat(name="Aerial Form",
                                         description="You learn a new form for your Wild Shape: Animal of the Sky."))

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Aerial Form",
                                         description="You gain the ability to become a Tiny creature. When you "
                                                     "transform into a Wild Shape form, you can make it Tiny. If you "
                                                     "do so, you can stay in that form no longer than 10 minutes, and "
                                                     "the damage you deal in that form is halved."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        self._features.append(feats.Feat(name="Alternating Forms",
                                         description="You can now rapidly shift between a Wild Shape form and your "
                                                     "normal form. If you're in a Wild Shape form, you can switch to "
                                                     "your normal form as a Bonus Action, and you can then switch back "
                                                     "into that Wild Shape form within the next minute as a Bonus "
                                                     "Action. Neither switch expends a use of Wild Shape."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Wild Resurgence",
                                         description="When you use your Wild Shape, primal magic radiates from you, "
                                                     "allowing you to use Healing Blossoms as part of the same use of"
                                                     "Channel Nature."))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        self._features.append(feats.Feat(name="Beast Spells",
                                         description="You can cast spells in any Wild Shape form. While in such a "
                                                     "form, you can perform Somatic and Verbal Components, "
                                                     "and you don't need to provide free Material Components. If a "
                                                     "spell consumes its Material Component, you can't cast that "
                                                     "spell while in a Wild Shape form."))

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Archdruid",
                                         description="Whenever you roll Initiative, you regain one use of your Channel "
                                                     "Nature.\n"
                                                     "In addition, the primal magic that you wield causes you to age "
                                                     "more slowly. For every 10 years that pass, your body ages only 1 "
                                                     "year."))

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
                SpellLists.PRIMAL in spell().get_spell_lists()]

    def get_spellcasting_class(self) -> str | None:
        return "Druid"

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
                             feats.Feat(name="Lay on Hands",
                                        description="Your blessed touch can heal wounds. You have a pool of healing "
                                                    "power that replenishes when you take a Long Rest. With that pool, "
                                                    "you can restore a total number of Hit Points equal to five times "
                                                    "your Paladin level.\n"
                                                    "As a Magic action, you can touch a creature (which could be "
                                                    "yourself) and draw power from the pool of healing to restore a "
                                                    "number of Hit Points to that creature, up to the maximum amount "
                                                    "remaining in the pool.\n"
                                                    "In addition, you can expend 5 Hit Points from the pool of healing "
                                                    "to remove the Poisoned condition from the creature, rather than "
                                                    "using those points to restore Hit Points."),
                             feats.Feat(name="Spellcasting",
                                        description="Spell Preparation. Any Spell you prepare for this Class must be "
                                                    "a Divine Spell.\n"
                                                    "Whenever you finish a Long Rest, you can meditate and replace any "
                                                    "Spell you have prepared for this Class with another Divine Spell "
                                                    "of the same level.\n"
                                                    "Your spell slots determine the number of different Spells you "
                                                    "can prepare of each level.\n"
                                                    "Spellcasting Ability. Charisma is your Spellcasting Ability for "
                                                    "your Paladin Spells.\n"
                                                    "Spellcasting Focus. You can use a Holy Symbol as a Spellcasting "
                                                    "Focus for the Spells you prepare for this Class.")
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

        self._features.append(feats.Feat(name="Divine Smite",
                                         description="When you strike a target, you can channel divine energy to smite "
                                                     "it. Immediately after you hit a target with an attack roll using "
                                                     "a weapon or an Unarmed Strike, you can expend one Spell Slot to "
                                                     "deal Radiant damage to the target. The damage is 2d8 for a "
                                                     "1st-level Spell Slot, plus 1d8 for each slot level higher than "
                                                     "1st.\n"
                                                     "You can use Divine Smite no more than once during a turn, and "
                                                     "you can't use it on the same turn that you cast a spell."))
        self._features.append(fighting_style)

    def _level_up_3(self, content: dict[str, dict[str, any]]):
        del content
        self._features.append(feats.Feat(name="Channel Divinity",
                                         description="You can channel divine energy directly from the Outer Planes, "
                                                     "using that energy to fuel magical effects. You start with one "
                                                     "such effect: Divine Sense, which is described below. Other "
                                                     "Paladin features give additional Channel Divinity effect "
                                                     "options. Each time you use this Channel Divinity, you choose "
                                                     "which effect to create from among those you have from this "
                                                     "class.\n"
                                                     "You can use Channel Divinity twice. You regain one expended use "
                                                     "when you finish a Short Rest, and you regain all expended uses "
                                                     "when you finish a Long Rest. You gain additional uses when you "
                                                     "reach certain Paladin levels, as shown in the Channel Divinity "
                                                     "column of the Paladin table.\n"
                                                     "If a Channel Divinity effect requires a saving throw, the DC "
                                                     "equals the Spell Save DC from this class's Spellcasting "
                                                     "feature.\n"
                                                     "Divine Sense. As a Bonus Action, you can open your awareness to "
                                                     "detect Celestials, Fiends, and Undead. For the next 10 minutes "
                                                     "or until you have the Incapacitated condition, you know the "
                                                     "location of any creature of those types within 60 feet of "
                                                     "yourself, and you know its creature type. Within the same "
                                                     "radius, you also detect the presence of any place or object that "
                                                     "has been consecrated or desecrated, as with the Hallow spell."))

    def _level_up_4(self, feat: feats.Feat):
        if feat.get_level() > 4:
            raise Exception("Invalid feat level. Must be 4 or lower")

        self._features.append(feat)

    def _level_up_5(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Extra Attack",
                                         description="You can attack twice, instead of once, whenever you take the "
                                                     "Attack Action on your turn."))
        self._features.append(feats.Feat(name="Faithful Steed",
                                         description="You can easily call on the aid of an otherworldly steed. You "
                                                     "always have the Find Steed spell prepared, and it doesn't count "
                                                     "against the number of spells you can prepare.\n"
                                                     "When you cast this spell, its casting time is an action. You can "
                                                     "also cast the spell once without expending a Spell Slot, and "
                                                     "you regain the ability to do so when you finish a Long Rest.",
                                         feat_spells=content["Spells"]["Find Steed"]()))

    def _level_up_7(self):
        self._features.append(feats.Feat(name="Aura of Protection",
                                         description="You radiate a protective, invisible aura that extends 10 feet "
                                                     "from you in every direction, but it doesn't extend through "
                                                     "Total Cover.\n"
                                                     "You and your allies in the aura gain a bonus to saving throws "
                                                     "equal to your Charisma modifier (minimum bonus of +1).\n"
                                                     "If another Paladin is present, a creature can benefit from only "
                                                     "one Aura of Protection at a time; the creature chooses which "
                                                     "one when entering the auras."))
        # TODO Implement Saving throw increase on self

    def _level_up_8(self, feat: feats.Feat):
        if feat.get_level() > 8:
            raise Exception("Invalid feat level. Must be 8 or lower")

        self._features.append(feat)

    def _level_up_9(self):
        self._features.append(feats.Feat(name="Abjure Foes",
                                         description="As a Magic action, you can expend one use of your Channel "
                                                     "Divinity to overwhelm foes with divine awe. As you present your "
                                                     "Holy Symbol or weapon, you can target a number of creatures "
                                                     "equal to your Charisma modifier (minimum of one creature) that "
                                                     "you can see within 60 feet of yourself.\n"
                                                     "Each target must make a Wisdom saving throw. On a failed save, "
                                                     "the target has the Dazed and Frightened conditions for 1 minute "
                                                     "or until it takes any damage. On a successful save, the target "
                                                     "has the Dazed condition for 1 minute or until it takes any "
                                                     "damage."))

    def _level_up_11(self):
        self._features.append(feats.Feat(name="Radiant Strikes",
                                         description="You are so suffused with divine might that your weapon strikes "
                                                     "carry supernatural power with them. When you hit a target with "
                                                     "an attack roll using a Simple or Martial weapon, the target "
                                                     "takes an extra 1d8 Radiant damage."))

    def _level_up_12(self, feat: feats.Feat):
        if feat.get_level() > 12:
            raise Exception("Invalid feat level. Must be 12 or lower")

        self._features.append(feat)

    def _level_up_13(self):
        self._features.append(feats.Feat(name="Aura of Courage",
                                         description="You and your allies are immune to the Frightened condition while "
                                                     "in your Aura of Protection. If a Frightened ally enters the "
                                                     "aura, that condition is suppressed while the ally is there."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Restoring Touch",
                                         description="When you use Lay on Hands on a creature, you can also remove one "
                                                     "or more of the following conditions from the creature: Blinded, "
                                                     "Charmed, Dazed, Deafened, Frightened, Paralyzed, or Stunned. You "
                                                     "must expend 5 Hit Points from the healing pool of Lay on Hands "
                                                     "for each of these conditions you remove; those points don't also "
                                                     "restore Hit Points to the creature."))

    def _level_up_16(self, feat: feats.Feat):
        if feat.get_level() > 16:
            raise Exception("Invalid feat level. Must be 16 or lower")

        self._features.append(feat)

    def _level_up_17(self):
        self._features.append(feats.Feat(name="Aura Expansion",
                                         description="Your Aura of Protection now extends 30 feet from you rather than "
                                                     "10 feet."))

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Divine Conduit",
                                         description="Whenever you roll Initiative, you regain one use of this class's "
                                                     "Channel Divinity."))

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
                SpellLists.DIVINE in spell().get_spell_lists()]

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
