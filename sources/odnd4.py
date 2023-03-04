"""
Content from the Dungeons and Dragons OneD&D Character Origins Unearthed Arcana.
https://media.dndbeyond.com/compendium-images/one-dnd/druid-paladin/PXoa3UgywnZbwc9U/UA-2023-DruidandPaladin.pdf
"""

from rules import abilities, classes, feats, spells
from rules.enums import AbilityNames, SpellLists, SpellSchools


class MoonDruid(classes.Druid):
    """
    Circle of The Moon subclass for Druid
    UA p. 8
    """

    def __init__(self, **kwargs):
        super().__init__(name="Moon Druid", **kwargs)

    def _level_up_3(self):
        self._features.append(feats.Feat(name="Combat Wild Shape",
                                         description="You have learned magical techniques that allow you to transform "
                                                     "quickly and to channel magical protection while transformed, "
                                                     "giving you these benefits:\n"
                                                     "Abjuration Spells. While you're in a Wild Shape form, you can "
                                                     "cast any spell you currently have prepared from the Abjuration "
                                                     "School, provided the spell doesn't require a material "
                                                     "component.\n"
                                                     "Quick Attack. You can use Unarmed Strike as a Bonus Action.\n"
                                                     "Swift Transformation. You can use your Wild Shape as a Bonus "
                                                     "Action or Magic action, but no more than once on a turn."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Elemental Wild Shape",
                                         description="Channeling ancient lunar magic, you imbue your Wild Shape forms "
                                                     "with power from the Elemental Planes. Whenever you assume a "
                                                     "Wild Shape form, choose one of the following damage types: Acid, "
                                                     "Cold, Fire, Lightning, or Thunder.\n"
                                                     "While in that form, you have Resistance to the chosen damage "
                                                     "type, and the form's Bestial Strike can deal damage of that type "
                                                     "rather than its normal type - with you choosing between the "
                                                     "types when you hit.\n"
                                                     "Your form also displays signs of the chosen damage type. For "
                                                     "example, if you choose Fire, your fur in Wild Shape might "
                                                     "flicker with harmless flames. You choose the details."))

    def _level_up_10(self):
        self._features.append(feats.Feat(name="Elemental Strike",
                                         description="Elemental forces imbue your attacks. When you deal damage with "
                                                     "your Bestial Strike, the target takes an extra 1d6 damage of the "
                                                     "type you chose from Elemental Wild Shape. This extra damage "
                                                     "increases to 2d6 when you reach 17th level in this class."))

    def _level_up_14(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Thousand Forms",
                                         description="You have learned to use lunar magic to alter your physical form "
                                                     "in innumerable ways. You always have the Alter Self spell "
                                                     "prepared, and you can cast it without expending a Spell Slot. It "
                                                     "also doesn't count against the number of spells you have "
                                                     "prepared.",
                                         feat_spells=[content["Spells"]["Alter Self"]()]))


class DevotionPaladin(classes.Paladin):
    """
    Oath of Devotion subclass for Paladin
    UA p. 13-14
    """

    def __init__(self, **kwargs):
        super().__init__(name="Devotion Paladin", **kwargs)

    def _level_up_3(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Oath Spells",
                                         description="The magic of your oath gives you the following benefits:\n"
                                                     "Prepared Spells. You always have certain spells ready; when you "
                                                     "reach a Paladin level specified in the Oath of Devotion Spells "
                                                     "table, you thereafter always have the listed spells prepared. "
                                                     "These spells don't count against the number of spells you can "
                                                     "prepare, and they follow the rules of this class's Spellcasting "
                                                     "feature.\n"
                                                     "Free Casting. You can cast one of your prepared spells from this "
                                                     "feature without expending a Spell Slot, and you must finish a "
                                                     "Long Rest before you use this benefit again.",
                                         feat_spells=[
                                             content["Spells"]["Protection from Evil and Good"](
                                             ),
                                             content["Spells"]["Shield of Faith"](),
                                             content["Spells"]["Aid"](),
                                             content["Spells"]["Zone of Truth"](),
                                             content["Spells"]["Aura of Vitality"](),
                                             content["Spells"]["Blinding Smite"](),
                                             content["Spells"]["Guardian of Faith"](
                                             ),
                                             content["Spells"]["Staggering Smite"](),
                                             content["Spells"]["Commune"](),
                                             content["Spells"]["Flame Strike"](),
                                         ],
                                         spellcasting_ability=AbilityNames.CHARISMA))
        self._features.append(feats.Feat(name="Sacred Weapon",
                                         description="As a Bonus Action, you can expend one use of your Channel "
                                                     "Divinity to imbue one Simple or Martial weapon that you are "
                                                     "holding with positive energy. For 1 minute, you add your "
                                                     "Charisma modifier to attack rolls you make with that weapon "
                                                     "(minimum bonus of +1), and each time you hit with it, you cause "
                                                     "it to deal its normal damage type or Radiant damage.\n"
                                                     "The weapon also emits bright light in a 20-foot radius and dim "
                                                     "light 20 feet beyond that.\n"
                                                     "You can end this effect as a Bonus Action. This effect also ends "
                                                     "if you aren't holding or carrying the weapon or if you have the "
                                                     "Incapacitated condition."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Smite of Protection",
                                         description="Your Divine Smite now radiates protective energy that allows you "
                                                     "and your allies to stay in the fight. Whenever you use your "
                                                     "Divine Smite, choose yourself or an ally within 30 feet of "
                                                     "yourself. The chosen creature gains Temporary Hit Points equal "
                                                     "to 1d8 plus the level of the Spell Slot used for the Divine "
                                                     "Smite."))

    def _level_up_10(self):
        self._features.append(feats.Feat(name="Aura of Devotion",
                                         description="You and your allies are immune to the Charmed condition while in "
                                                     "your Aura of Protection. If a Charmed ally enters the aura, that "
                                                     "condition is suppressed while the ally is there."))

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Holy Nimbus",
                                         description="As a Bonus Action, you can imbue your Aura of Protection with "
                                                     "holy power. The aura gains the following benefits for 1 minute "
                                                     "or until you end them as a Bonus Action:\n"
                                                     "Radiant Damage. Whenever an enemy starts its turn in the aura, "
                                                     "that creature takes Radiant damage equal to your Proficiency "
                                                     "Bonus plus your Charisma modifier.\n"
                                                     "Sunlight. The aura is filled with bright light that is "
                                                     "sunlight.\n"
                                                     "Once you use this feature, you can't use it again until you "
                                                     "finish a Long Rest unless you expend a Spell Slot of at least "
                                                     "4th level when you use it again."))


class EpicAbilityScoreImprovement(feats.Feat):
    """
    Epic Ability Score Improvement Feat
    UA p. 6
    """

    def __init__(self, ability: AbilityNames):
        super().__init__(name="Epic Ability Score Improvement",
                         description=f"You increase {ability.value} by 2. This increase can raise the score above"
                                     "20 but not above 30.",  # TODO epic increase
                         level=4,
                         repeatable="Yes",
                         feat_abilities=abilities.Abilities(
                             strength=2 if ability == AbilityNames.STRENGTH else 0,
                             dexterity=2 if ability == AbilityNames.DEXTERITY else 0,
                             constitution=2 if ability == AbilityNames.CONSTITUTION else 0,
                             intelligence=2 if ability == AbilityNames.INTELLIGENCE else 0,
                             wisdom=2 if ability == AbilityNames.WISDOM else 0,
                             charisma=2 if ability == AbilityNames.CHARISMA else 0,
                         ),
                         visible=False)


class BanishingSmite(spells.Spell):
    """
    Banishing Smite Spell
    UA p. 18
    """

    def __init__(self):
        super().__init__(name="Banishing Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=5,
                         school=SpellSchools.CONJURATION,
                         casting_time="Bonus Action, which you take immediately after hitting a creature with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         duration="1 minute",
                         description="The target hit by the strike takes an extra 5d10 Force damage, and the target "
                                     "must succeed on a Charisma saving throw or be transported to a harmless "
                                     "demiplane for the duration.\n"
                                     "While in the demiplane, the target has the Incapacitated condition. At the end "
                                     "of each of its turns, the target repeats the save, ending the spell on itself on "
                                     "a success. When the spell ends on the target, it reappears in the space it left "
                                     "or in the nearest unoccupied space if that space is occupied.\n"
                                     "If the spell lasts on the target for 1 minute and the target is an Aberration, a "
                                     "Celestial, an Elemental, a Fey, or a Fiend, the target doesn't return. It is "
                                     "instead transported to a random location on a plane associated with its creature "
                                     "type.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 6th level or higher, the "
                                          "extra damage increases by 1d10 for each slot level above 5th.")


class BlindingSmite(spells.Spell):
    """
    Blinding Smite Spell
    UA p. 18
    """

    def __init__(self):
        super().__init__(name="Blinding Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=3,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="Bonus Action, which you take immediately after hitting a creature with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         duration="1 minute",
                         description="The target hit by the strike takes an extra 3d8 Radiant damage, and the target "
                                     "must succeed on a Constitution saving throw or have the Blinded condition until "
                                     "the spell ends. At the end of each of its turns, the Blinded target repeats the "
                                     "saving throw, ending the spell on itself on a success.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 4th level or higher, the "
                                          "extra damage increases by 1d8 for each slot level above 3rd.")


class FindFamiliar(spells.Spell):
    """
    Find Familiar Spell
    UA p. 18-19
    """

    def __init__(self):
        super().__init__(name="Find Familiar",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.CONJURATION,
                         ritual=True,
                         casting_time="1 hour",
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="10 GP worth of charcoal, incense, and herbs that must be consumed "
                                                  "by fire in a brass brazier",
                         description="You gain the service of an otherworldly spirit, which manifests as a little "
                                     "animal in an unoccupied space of your choice within range. This creature uses "
                                     "the Otherworldly Familiar stat block. If you already have a familiar from this "
                                     "spell, that familiar transforms into the new one but retains its memories; you "
                                     "don't get a second familiar.\n"
                                     "Whenever you cast the spell, choose the familiar's creature type: Celestial, "
                                     "Fey, or Fiend. Also choose an environment: Air, Land, or Water. The familiar "
                                     "resembles a Tiny animal of your choice - such as an owl, a cat, or a frog - that "
                                     "is native to the chosen environment. Both choices - creature type and environment"
                                     " - determine certain traits in the stat block.\n"
                                     "Combat. The familiar is an ally to you and your companions. In combat, it shares "
                                     "your initiative count, but it takes its turn immediately after yours. It obeys "
                                     "your commands (no action required by you), but the familiar can't attack unless "
                                     "you use your Reaction on its turn to command it do so.\n"
                                     "If you don't issue any commands, the familiar takes the Dodge action and uses "
                                     "its Move to avoid danger.\n"
                                     "Disappearance of the Familiar. The familiar disappears if it drops to 0 Hit "
                                     "Points, if you dismiss it as a Bonus Action, or if you die. When it disappears, "
                                     "it leaves behind anything it was wearing or carrying. If you cast this spell "
                                     "again, you decide whether you summon the familiar that disappeared or a "
                                     "different one.\n"
                                     "Remote Viewing. As a Magic action, you can see what your familiar sees and hear "
                                     "what it hears until the end of your next turn.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 2nd level or higher, use "
                                          "the higher level wherever the spell's level appears in the stat block.")


class FindSteed(spells.Spell):
    """
    Find Steed Spell
    UA p. 19-20
    """

    def __init__(self):
        super().__init__(name="Find Steed",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.CONJURATION,
                         casting_time="10 minutes",
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You gain the service of an otherworldly being, which manifests as a loyal steed "
                                     "in an unoccupied space of your choice within range. This creature uses the "
                                     "Otherworldly Steed stat block. If you already have a steed from this spell, your "
                                     "steed is replaced by the new one.\n"
                                     "The steed resembles a Large, rideable animal of your choice, such as a horse, a "
                                     "camel, a dire wolf, or an elk. Whenever you cast the spell, choose the steed's "
                                     "creature type - Celestial, Fey, or Fiend - which determines certain traits in "
                                     "the stat block.\n"
                                     "Combat. The steed is an ally to you and your companions. In combat, it shares "
                                     "your initiative count, and it functions as a controlled mount (as defined in the "
                                     "rules on mounted combat). If you have the Incapacitated condition, it takes its "
                                     "turn immediately after yours and acts independently, focusing on protecting "
                                     "you.\n"
                                     "Disappearance of the Steed. The steed disappears if it drops to 0 Hit Points, if "
                                     "you dismiss it as a Bonus Action, or if you die. When it disappears, it leaves "
                                     "behind anything it was wearing or carrying. If you cast this spell again, you "
                                     "decide whether you summon the steed that disappeared or a different one.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 3rd level or higher, use the "
                                          "higher level wherever the spell's level appears in the stat block.")


class GlimmeringSmite(spells.Spell):
    """
    Glimmering Smite Spell
    UA p. 20
    """

    def __init__(self):
        super().__init__(name="Glimmering Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="Bonus Action, which you take immediately after hitting a creature with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="The target hit by the strike takes an extra 2d6 Radiant damage, and if has the "
                                     "Invisible condition, that condition ends on it. In addition, until the spell "
                                     "ends, the target sheds bright light in a 5-foot radius, and attack rolls against "
                                     "it have Advantage.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 3rd level or higher, the "
                                          "extra damage increases by 1d6 for each slot level above 2nd.")


class SearingSmite(spells.Spell):
    """
    Searing Smite Spell
    UA p. 20
    """

    def __init__(self):
        super().__init__(name="Searing Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.EVOCATION,
                         casting_time="Bonus Action, which you take immediately after hitting a target with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="As you hit the target, your strike flares with white-hot intensity, and the "
                                     "target takes an extra 1d6 Fire damage and ignites with magical fire. At the "
                                     "start of each of its turns until the spell ends, the target must make a "
                                     "Constitution saving throw. On a failed save, it takes 1d6 Fire damage. On a "
                                     "successful save, the spell ends.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 2nd level or higher, the "
                                          "damage increases by 1d6 for each slot level above 1st.")


class SpareTheDying(spells.Spell):
    """
    Spare the Dying Spell
    UA p. 20
    """

    def __init__(self):
        super().__init__(name="Spare the Dying",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.NECROMANCY,
                         casting_time="Action",
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="You touch a creature that has the Dying condition. The creature regains 1 Hit "
                                     "Point.")


class StaggeringSmite(spells.Spell):
    """
    Staggering Smite Spell
    UA p. 20
    """

    def __init__(self):
        super().__init__(name="Staggering Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=4,
                         school=SpellSchools.ENCHANTMENT,
                         casting_time="Bonus Action, which you take immediately after hitting a creature with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         description="As you hit the creature, your strike pierces both body and mind. The target "
                                     "takes an extra 4d6 Psychic damage, and the target must succeed on a Wisdom "
                                     "saving throw or have the Stunned condition until the end of your next turn.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 5th level or higher, the "
                                          "extra damage increases by 1d6 for each slot level above 4th.")


class ThunderousSmite(spells.Spell):
    """
    Thunderous Smite Spell
    UA p. 21
    """

    def __init__(self):
        super().__init__(name="Thunderous Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="Bonus Action, which you take immediately after hitting a target with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         description="As you hit the target, your strike rings with thunder that is audible within 300 "
                                     "feet of you, and the target takes an extra 2d6 Thunder damage. Additionally, if "
                                     "the target is a creature, it must succeed on a Strength saving throw or be "
                                     "pushed 10 feet away from you and have the Prone condition.",
                         at_higher_levels="When you cast this spell using a Spell Slot of 2nd level or higher, the "
                                          "damage increases by 1d6 for each slot level above 1st.")


class WrathfulSmite(spells.Spell):
    """
    Wrathful Smite Spell
    UA p. 21
    """

    def __init__(self):
        super().__init__(name="Wrathful Smite",
                         spell_lists=[SpellLists.DIVINE],
                         level=1,
                         school=SpellSchools.ENCHANTMENT,
                         casting_time="Bonus Action, which you take immediately after hitting a creature with a weapon "
                                      "or an Unarmed Strike",
                         spell_range="Self",
                         verbal_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="As you hit the creature, it takes an extra 1d6 Psychic damage, and it must "
                                     "succeed on a Wisdom saving throw or have the Frightened condition until the "
                                     "spell ends. At the end of each of its turns, the Frightened target repeats the "
                                     "saving throw, ending the spell on itself on a success",
                         at_higher_levels=" When you cast this spell using a Spell Slot of 2nd level or higher, the "
                                          "damage increases by 1d6 for each slot level above 1st.")


CONTENT = {
    "Classes": {
        "Moon Druid": MoonDruid,
        "Devotion Paladin": DevotionPaladin,
    },
    "Feats": {
        # TODO The rest of the feats
        "Epic Ability Score Improvement": EpicAbilityScoreImprovement,
        # "Epic Boon of Fate": EpicBoonFate,
        # "Epic Boon of Spell Recall": EpicBoonSpellRecall,
        # "Epic Boon of Truesight": EpicBoonTruesight,
    },
    "Spells": {
        "Banishing Smite": BanishingSmite,
        "Blinding Smite": BlindingSmite,
        "Find Familiar": FindFamiliar,
        "Find Steed": FindSteed,
        "Glimmering Smite": GlimmeringSmite,
        "Searing Smite": SearingSmite,
        "Spare the Dying": SpareTheDying,
        "Staggering Smite": StaggeringSmite,
        "Thunderous Smite": ThunderousSmite,
        "Wrathful Smite": WrathfulSmite,
    }
}
