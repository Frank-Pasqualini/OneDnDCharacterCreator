"""
Content from the Dungeons and Dragons System Reference Document v5.1.
https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf
"""
from rules import armors, bonuses, classes, feats, spells, weapons
from rules.enums import ArmorTraining, DamageTypes, ProficiencyLevels, Skills, SpellLists, SpellSchools, WeaponTypes


class Padded(armors.Armor):
    """
    Padded Armor
    SRD p. 63
    """

    def __init__(self):
        super().__init__(name="Padded",
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=11,
                         stealth_disadvantage=True)


class Leather(armors.Armor):
    """
    Leather Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Leather",
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=11)


class StuddedLeather(armors.Armor):
    """
    Studded Leather Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Studded Leather",
                         training_needed=ArmorTraining.LIGHT,
                         armor_class=12)


class Hide(armors.Armor):
    """
    Hide Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Hide",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=12)


class ChainShirt(armors.Armor):
    """
    Chain Shirt Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Chain Shirt",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=13)


class ScaleMail(armors.Armor):
    """
    Scale Mail Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Scale Mail",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=14,
                         stealth_disadvantage=True)


class Breastplate(armors.Armor):
    """
    Breastplate Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Breastplate",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=14)


class HalfPlate(armors.Armor):
    """
    Half Plate Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Half Plate",
                         training_needed=ArmorTraining.MEDIUM,
                         armor_class=15,
                         stealth_disadvantage=True)


class RingMail(armors.Armor):
    """
    Ring Mail Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Ring Mail",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=14,
                         stealth_disadvantage=True)


class ChainMail(armors.Armor):
    """
    Chain Mail Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Chain Mail",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=16,
                         stealth_disadvantage=True)


class Splint(armors.Armor):
    """
    Splint Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Splint",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=17,
                         stealth_disadvantage=True)


class Plate(armors.Armor):
    """
    Plate Armor
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Plate",
                         training_needed=ArmorTraining.HEAVY,
                         armor_class=18,
                         stealth_disadvantage=True)


class Shield(armors.Armor):
    """
    Shield
    SRD p. 64
    """

    def __init__(self):
        super().__init__(name="Shield",
                         training_needed=ArmorTraining.SHIELD,
                         armor_class=2)


class ChampionFighter(classes.Fighter):
    """
    Champion subclass for Fighter
    SRD p. 25
    """

    def __init__(self, **kwargs):
        super().__init__(name="Champion Fighter", **kwargs)

    def _level_up_3(self):
        self._features.append(feats.Feat(name="Improved Critical",
                                         description="Your weapon attacks score a critical hit on a roll of 19 or 20."))

    def _level_up_7(self):
        self._features.append(feats.Feat(name="Remarkable Athlete",
                                         description="You can add half your proficiency bonus (round up) to any "
                                                     "Strength, Dexterity, or Constitution check you make that "
                                                     "doesn't already use your proficiency bonus.\n"
                                                     "In addition, when you make a running long jump, the distance "
                                                     "you can cover increases by a number of feet equal to your "
                                                     "Strength modifier.",
                                         feat_bonuses=bonuses.Bonuses(
                                             skills={
                                                 Skills.ACROBATICS: ProficiencyLevels.HALF,
                                                 Skills.ATHLETICS: ProficiencyLevels.HALF,
                                                 Skills.SLEIGHT_OF_HAND: ProficiencyLevels.HALF,
                                                 Skills.STEALTH: ProficiencyLevels.HALF,
                                             },
                                             initiative=ProficiencyLevels.HALF)))

    def _level_up_10(self, fighting_style: feats.FightingStyle):
        if fighting_style.get_level() > 10:
            raise Exception("Invalid feat level. Must be 10 or lower")

        self._features.append(fighting_style)

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Superior Critical",
                                         description="Your weapon attacks score a critical hit on a roll of 18-20."))

    def _level_up_18(self):
        self._features.append(feats.Feat(name="Survivor",
                                         description="You attain the pinnacle of resilience in battle. At the start "
                                                     "of each of your turns, you regain hit points equal to 5 + your "
                                                     "Constitution modifier if you have no more than half of your hit "
                                                     "points left. You don’t gain this benefit if you have 0 hit "
                                                     "points."))


class DevotionPaladin(classes.Paladin):
    """
    Oath of Devotion subclass for Paladin
    SRD p. 25
    """

    def __init__(self, **kwargs):
        super().__init__(name="Oath of Devotion Paladin", **kwargs)

    def _level_up_3(self, content: dict[str, dict[str, any]]):
        super()._level_up_3(content)
        self._features.append(feats.Feat(name="Channel Divinity",
                                         description="When you use your Channel Divinity, you choose which option to "
                                                     "use. You must then finish a short or long rest to use your "
                                                     "Channel Divinity again.\n"
                                                     "Sacred Weapon. As an action, you can imbue one weapon that you "
                                                     "are holding with positive energy, using your Channel Divinity. "
                                                     "For 1 minute, you add your Charisma modifier to attack rolls "
                                                     "made with that weapon (with a minimum bonus of +1). The weapon "
                                                     "also emits bright light in a 20-foot radius and dim light 20 "
                                                     "feet beyond that. If the weapon is not already magical, "
                                                     "it becomes magical for the duration.\n"
                                                     "You can end this effect on your turn as part of any other "
                                                     "action. If you are no longer holding or carrying this weapon, "
                                                     "or if you fall unconscious, this effect ends.\n"
                                                     "Turn the Unholy. As an action, you present your holy symbol and "
                                                     "speak a prayer censuring fiends and undead, using your Channel "
                                                     "Divinity. Each fiend or undead that can see or hear you within "
                                                     "30 feet of you must make a Wisdom saving throw. If the creature "
                                                     "fails its saving throw, it is turned for 1 minute or until it "
                                                     "takes damage.\n"
                                                     "A turned creature must spend its turns trying to move as far "
                                                     "away from you as it can, and it can’t willingly move to a space "
                                                     "within 30 feet of you. It also can’t take reactions. For its "
                                                     "action, it can use only the Dash action or try to escape from "
                                                     "an effect that prevents it from moving. If there’s nowhere to "
                                                     "move, the creature can use the Dodge action."))
        self._features.append(feats.Feat(name="Oath Spells",
                                         description="You gain access to these spells at the levels specified in the "
                                                     "oath description. Once you gain access to an oath spell, you "
                                                     "always have it prepared. Oath spells don’t count against the "
                                                     "number of spells you can prepare each day.",
                                         feat_spells=[
                                             content["Spells"]["Protection from Evil and Good"](
                                             ),
                                             content["Spells"]["Sanctuary"](),
                                             content["Spells"]["Lesser Restoration"](
                                             ),
                                             content["Spells"]["Zone of Truth"](),
                                             content["Spells"]["Beacon of Hope"](),
                                             content["Spells"]["Dispel Magic"](),
                                             content["Spells"]["Freedom of Movement"](
                                             ),
                                             content["Spells"]["Guardian of Faith"](
                                             ),
                                             content["Spells"]["Commune"](),
                                             content["Spells"]["Flame Strike"](),
                                         ],
                                         visible=False))

    def _level_up_7(self):
        self._features.append(feats.Feat(name="Aura of Devotion",
                                         description="You and friendly creatures within 10 feet of you can’t be "
                                                     "charmed while you are conscious.\n"
                                                     "At 18th level, the range of this aura increases to 30 feet."))

    def _level_up_15(self):
        self._features.append(feats.Feat(name="Purity of Spirit",
                                         description="You are always under the effects of a protection from evil and "
                                                     "good spell."))

    def _level_up_20(self):
        self._features.append(feats.Feat(name="Holy Nimbus",
                                         description="As an action, you can emanate an aura of sunlight. For 1 minute, "
                                                     "bright light shines from you in a 30-foot radius, and dim light "
                                                     "shines 30 feet beyond that.\n"
                                                     "Whenever an enemy creature starts its turn in the bright light, "
                                                     "the creature takes 10 radiant damage.\n"
                                                     "In addition, for the duration, you have advantage on saving "
                                                     "throws against spells cast by fiends or undead.\n"
                                                     "Once you use this feature, you can’t use it again until you "
                                                     "finish a long rest."))


class AnimalFriendship(spells.Spell):
    """
    Animal Friendship Spell
    SRD p. 115
    """

    def __init__(self):
        super().__init__(name="Animal Friendship",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ENCHANTMENT,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a morsel of food",
                         duration="24 hours",
                         description="This spell lets you convince a beast that you mean it no harm. Choose a beast "
                                     "that you can see within range. It must see and hear you. If the beast's "
                                     "Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed "
                                     "on a Wisdom saving throw or be charmed by you for the spell's duration. If you "
                                     "or one of your companions harms the target, the spells ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you can affect one additional beast t level above 1st.")


class AnimalMessenger(spells.Spell):
    """
    Animal Messenger Spell
    SRD p. 115
    """

    def __init__(self):
        super().__init__(name="Animal Messenger",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ENCHANTMENT,
                         ritual=True,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a morsel of food",
                         duration="24 hours",
                         description="By means of this spell, you use an animal to deliver a message. Choose a Tiny "
                                     "beast you can see within range, such as a squirrel, a blue jay, or a bat. You "
                                     "specify a location, which you must have visited, and a recipient who matches a "
                                     "general description, such as “a man or woman dressed in the uniform of the town "
                                     "guard” or “a red-haired dwarf wearing a pointed hat.” You also speak a "
                                     "message of up to twenty-five words. The target beast travels for the duration "
                                     "of the spell toward the specified location, covering about 50 miles per 24 "
                                     "hours for a flying messenger, or 25 miles for other animals.\n"
                                     "When the messenger arrives, it delivers your message to the creature that you "
                                     "described, replicating the sound of your voice. The messenger speaks only to a "
                                     "creature matching the description you gave. If the messenger doesn't reach its "
                                     "destination before the spell ends, the message is lost, and the beast makes its "
                                     "way back to where you cast this spell.",
                         at_higher_levels="If you cast this spell using a spell slot of 3nd level or higher, "
                                          "the duration of the spell increases by 48 hours for each slot level above "
                                          "2nd.")


class Augury(spells.Spell):
    """
    Augury Spell
    SRD p. 120
    """

    def __init__(self):
        super().__init__(name="Augury",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         casting_time="1 minute",
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="specially marked sticks, bones, or similar tokens worth at least "
                                                  "25 gp",
                         description="By casting gem-inlaid sticks, rolling dragon bones, laying out ornate cards, "
                                     "or employing some other divining tool, you receive an omen from an otherworldly "
                                     "entity about the results of a specific course of action that you plan to take "
                                     "within the next 30 minutes. The DM chooses from the following possible omens:\n"
                                     "• Weal, for good results\n"
                                     "• Woe, for bad results\n"
                                     "• Weal and woe, for both good and bad results\n"
                                     "• Nothing, for results that aren't especially good or bad\n"
                                     "The spell doesn't take into account any possible circumstances that might "
                                     "change the outcome, such as the casting of additional spells or the loss or "
                                     "gain of a companion.\n"
                                     "If you cast the spell two or more times before completing your next long rest, "
                                     "there is a cumulative 25 percent chance for each casting after the first that "
                                     "you get a random reading. The DM makes this roll in secret.")


class ChillTouch(spells.Spell):
    """
    Chill Touch Spell
    SRD p. 124
    """

    def __init__(self):
        super().__init__(name="Chill Touch",
                         spell_lists=[SpellLists.ARCANE],
                         level=0,
                         school=SpellSchools.NECROMANCY,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         duration="1 round",
                         description="You create a ghostly, skeletal hand in the space of a creature within range. "
                                     "Make a ranged spell attack against the creature to assail it with the chill of "
                                     "the grave. On a hit, the target takes 1d8 necrotic damage, and it can't regain "
                                     "hit points until the start of your next turn. Until then, the hand clings to "
                                     "the target.\n"
                                     "If you hit an undead target, it also has disadvantage on attack rolls against "
                                     "you until the end of your next turn.\n"
                                     "This spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level "
                                     "(3d8), and 17th level (4d8).")


class CreateOrDestroyWater(spells.Spell):
    """
    Create or Destroy Water Spell
    SRD p. 132
    """

    def __init__(self):
        super().__init__(name="Create or Destroy Water",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a drop of water if creating water or a few grains of sand if "
                                                  "destroying it",
                         description="You either create or destroy water.\n"
                                     "Create Water. You create up to 10 gallons of clean water within range in an "
                                     "open container. Alternatively, the water falls as rain in a 30-foot cube within "
                                     "range, extinguishing exposed flames in the area.\n"
                                     "Destroy Water. You destroy up to 10 gallons of water in an open container "
                                     "within range. Alternatively, you destroy fog in a 30-foot cube within range.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you create or destroy 10 additional gallons of water, or the size of the "
                                          "cube increases by 5 feet, for each slot level above 1st.")


class CureWounds(spells.Spell):
    """
    Cure Wounds Spell
    SRD p. 132-133
    """

    def __init__(self):
        super().__init__(name="Cure Wounds",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ABJURATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="A creature you touch regains a number of hit points equal to 1d8 + your "
                                     "spellcasting ability modifier. This spell has no effect on undead or "
                                     "constructs.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the healing increases by 1d8 for each slot level above 1st.")


class Darkvision(spells.Spell):
    """
    Darkvision Spell
    SRD p. 133
    """

    def __init__(self):
        super().__init__(name="Darkvision",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="either a pinch of dried carrot or an agate",
                         duration="8 hours",
                         description="You touch a willing creature to grant it the ability to see in the dark. For "
                                     "the duration, that creature has darkvision out to a range of 60 feet.")


class DetectMagic(spells.Spell):
    """
    Detect Magic Spell
    SRD p. 134
    """

    def __init__(self):
        super().__init__(name="Detect Magic",
                         spell_lists=[SpellLists.ARCANE,
                                      SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="For the duration, you sense the presence of magic within 30 feet of you. If you "
                                     "sense magic in this way, you can use your action to see a faint aura around any "
                                     "visible creature or object in the area that bears magic, and you learn its "
                                     "school of magic, if any.\n"
                                     "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, "
                                     "1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.")


class DetectPoisonAndDisease(spells.Spell):
    """
    Detect Poison and Disease Spell
    SRD p. 134
    """

    def __init__(self):
        super().__init__(name="Detect Poison and Disease",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a yew leaf",
                         concentration=True,
                         duration="10 minutes",
                         description="For the duration, you can sense the presence and location of poisons, poisonous "
                                     "creatures, and diseases within 30 feet of you. You also identify the kind of "
                                     "poison, poisonous creature, or disease in each case.\n"
                                     "The spell can penetrate most barriers, but it is blocked by 1 foot of stone, "
                                     "1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.")


class DetectThoughts(spells.Spell):
    """
    False Life Spell
    SRD p. 135
    """

    def __init__(self):
        super().__init__(name="Detect Thoughts",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.DIVINATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a copper piece",
                         concentration=True,
                         duration="1 minute",
                         description="For the duration, you can read the thoughts of certain creatures. When you cast "
                                     "the spell and as your action on each turn until the spell ends, you can focus "
                                     "your mind on any one creature that you can see within 30 feet of you. If the "
                                     "creature you choose has an Intelligence of 3 or lower or doesn't speak any "
                                     "language, the creature is unaffected.\n"
                                     "You initially learn the surface thoughts of the creature—what is most on its "
                                     "mind in that moment. As an action, you can either shift your attention to "
                                     "another creature's thoughts or attempt to probe deeper into the same creature's "
                                     "mind. If you probe deeper, the target must make a Wisdom saving throw. If it "
                                     "fails, you gain insight into its reasoning (if any), its emotional state, "
                                     "and something that looms large in its mind (such as something it worries over, "
                                     "loves, or hates). If it succeeds, the spell ends. Either way, the target knows "
                                     "that you are probing into its mind, and unless you shift your attention to "
                                     "another creature's thoughts, the creature can use its action on its turn to "
                                     "make an Intelligence check contested by your Intelligence check; if it "
                                     "succeeds, the spell ends.\n"
                                     "Questions verbally directed at the target creature naturally shape the course "
                                     "of its thoughts, so this spell is particularly effective as part of an "
                                     "interrogation.\n"
                                     "You can also use this spell to detect the presence of thinking creatures you "
                                     "can't see. When you cast the spell or as your action during the duration, "
                                     "you can search for thoughts within 30 feet of you. The spell can penetrate "
                                     "barriers, but 2 feet of rock, 2 inches of any metal other than lead, "
                                     "or a thin sheet of lead blocks you. You can't detect a creature with an "
                                     "Intelligence of 3 or lower or one that doesn't speak any language.\n"
                                     "Once you detect the presence of a creature in this way, you can read its "
                                     "thoughts for the rest of the duration as described above, even if you can't see "
                                     "it, but it must still be within range.")


class Druidcraft(spells.Spell):
    """
    Druidcraft Spell
    SRD p. 138-139
    """

    def __init__(self):
        super().__init__(name="Druidcraft",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="Whispering to the spirits of nature, you create one of the following effects "
                                     "within range:\n"
                                     "• You create a tiny, harmless sensory effect that predicts what the weather "
                                     "will be at your location for the next 24 hours. The effect might manifest as a "
                                     "golden orb for clear skies, a cloud for rain, falling snowflakes for snow, "
                                     "and so on. This effect persists for 1 round.\n"
                                     "• You instantly make a flower blossom, a seed pod open, or a leaf bud bloom.\n"
                                     "• You create an instantaneous, harmless sensory effect, such as falling leaves, "
                                     "a puff of wind, the sound of a small animal, or the faint odor of skunk. The "
                                     "effect must fit in a 5-foot cube.\n"
                                     "• You instantly light or snuff out a candle, a torch, or a small campfire.")


class EnhanceAbility(spells.Spell):
    """
    Enhance Ability Spell
    SRD p. 139
    """

    def __init__(self):
        super().__init__(name="Longstrider",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="(fur or a feather from a beast",
                         concentration=True,
                         duration="1 hour",
                         description="You touch a creature and bestow upon it a magical enhancement. Choose one of "
                                     "the following effects; the target gains that effect until the spell ends.\n"
                                     "Bear's Endurance. The target has advantage on Constitution checks. It also "
                                     "gains 2d6 temporary hit points, which are lost when the spell ends.\n"
                                     "Bull's Strength. The target has advantage on Strength checks, and his or her "
                                     "carrying capacity doubles.\n"
                                     "Cat's Grace. The target has advantage on Dexterity checks. It also doesn't take "
                                     "damage from falling 20 feet or less if it isn't incapacitated.\n"
                                     "Eagle's Splendor. The target has advantage on Charisma checks.\n"
                                     "Fox's Cunning. The target has advantage on Intelligence checks.\n"
                                     "Owl's Wisdom. The target has advantage on Wisdom checks.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "you can target one additional creature for each slot level above 2nd.")


class EnlargeReduce(spells.Spell):
    """
    Enlarge/Reduce Spell
    SRD p. 140
    """

    def __init__(self):
        super().__init__(name="Enlarge/Reduce",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of powdered iron",
                         concentration=True,
                         duration="1 minute",
                         description="You cause a creature or an object you can see within range to grow larger or "
                                     "smaller for the duration. Choose either a creature or an object that is neither "
                                     "worn nor carried. If the target is unwilling, it can make a Constitution saving "
                                     "throw. On a success, the spell has no effect.\n"
                                     "If the target is a creature, everything it is wearing and carrying changes size "
                                     "with it. Any item dropped by an affected creature returns to normal size at "
                                     "once.\n"
                                     "Enlarge. The target's size doubles in all dimensions, and its weight is "
                                     "multiplied by eight. This growth increases its size by one category-- from "
                                     "Medium to Large, for example. If there isn't enough room for the target to "
                                     "double its size, the creature or object attains the maximum possible size in "
                                     "the space available. Until the spell ends, the target also has advantage on "
                                     "Strength checks and Strength saving throws. The target's weapons also grow to "
                                     "match its new size. While these weapons are enlarged, the target's attacks with "
                                     "them deal 1d4 extra damage.\n"
                                     "Reduce. The target's size is halved in all dimensions, and its weight is "
                                     "reduced to one-eighth of normal. This reduction decreases its size by one "
                                     "category--from Medium to Small, for example. Until the spell ends, the target "
                                     "also has disadvantage on Strength checks and Strength saving throws. The "
                                     "target's weapons also shrink to match its new size. While these weapons are "
                                     "reduced, the target's attacks with them deal 1d4 less damage (this can't reduce "
                                     "the damage below 1).")


class Entangle(spells.Spell):
    """
    Entangle Spell
    SRD p. 140
    """

    def __init__(self):
        super().__init__(name="Entangle",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.CONJURATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="Grasping weeds and vines sprout from the ground in a 20-foot square starting "
                                     "from a point within range. For the duration, these plants turn the ground in "
                                     "the area into difficult terrain.\n"
                                     "A creature in the area when you cast the spell must succeed on a Strength "
                                     "saving throw or be restrained by the entangling plants until the spell ends. A "
                                     "creature restrained by the plants can use its action to make a Strength check "
                                     "against your spell save DC. On a success, it frees itself.\n"
                                     "When the spell ends, the conjured plants wilt away.")


class FalseLife(spells.Spell):
    """
    False Life Spell
    SRD p. 142
    """

    def __init__(self):
        super().__init__(name="False Life",
                         spell_lists=[SpellLists.ARCANE],
                         level=1,
                         school=SpellSchools.NECROMANCY,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a small amount of alcohol or distilled spirits",
                         duration="1 hour",
                         description="Bolstering yourself with a necromantic facsimile of life, you gain 1d4 + 4 "
                                     "temporary hit points for the duration.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you gain 5 additional temporary hit points for each slot level above 1st.")


class FindTraps(spells.Spell):
    """
    Find Traps Spell
    SRD p. 144
    """

    def __init__(self):
        super().__init__(name="Find Traps",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.DIVINATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You sense the presence of any trap within range that is within line of sight. A "
                                     "trap, for the purpose of this spell, includes anything that would inflict a "
                                     "sudden or unexpected effect you consider harmful or undesirable, "
                                     "which was specifically intended as such by its creator. Thus, the spell would "
                                     "sense an area affected by the alarm spell, a glyph of warding, or a mechanical "
                                     "pit trap, but it would not reveal a natural weakness in the floor, an unstable "
                                     "ceiling, or a hidden sinkhole.\n"
                                     "This spell merely reveals that a trap is present. You don't learn the location "
                                     "of each trap, but you do learn the general nature of the danger posed by a trap "
                                     "you sense.")


class FogCloud(spells.Spell):
    """
    Fog Cloud Spell
    SRD p. 146
    """

    def __init__(self):
        super().__init__(name="Fog Cloud",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.CONJURATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You create a 20-foot-radius sphere of fog centered on a point within range. The "
                                     "sphere spreads around corners, and its area is heavily obscured. It lasts for "
                                     "the duration or until a wind of moderate or greater speed (at least 10 miles "
                                     "per hour) disperses it.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the radius of the fog increases by 20 feet for each slot level above 1st.")


class GentleRepose(spells.Spell):
    """
    Gentle Repose Spell
    SRD p. 148-149
    """

    def __init__(self):
        super().__init__(name="Gentle Repose",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.NECROMANCY,
                         ritual=True,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of salt and one copper piece placed on each of the "
                                                  "corpse's eyes, which must remain there for the duration",
                         duration="10 days",
                         description="You touch a corpse or other remains. For the duration, the target is protected "
                                     "from decay and can't become undead.\n"
                                     "The spell also effectively extends the time limit on raising the target from "
                                     "the dead, since days spent under the influence of this spell don't count "
                                     "against the time limit of spells such as raise dead.")


class Goodberry(spells.Spell):
    """
    Goodberry Spell
    SRD p. 150
    """

    def __init__(self):
        super().__init__(name="Goodberry",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a sprig of mistletoe",
                         description="Up to ten berries appear in your hand and are infused with magic for the "
                                     "duration. A creature can use its action to eat one berry. Eating a berry "
                                     "restores 1 hit point, and the berry provides enough nourishment to sustain a "
                                     "creature for one day.\n"
                                     "The berries lose their potency if they have not been consumed within 24 hours "
                                     "of the casting of this spell.")


class HealingWord(spells.Spell):
    """
    Healing Word Spell
    SRD p. 153
    """

    def __init__(self):
        super().__init__(name="Healing Word",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.ABJURATION,
                         casting_time="1 bonus action",
                         spell_range="60 feet",
                         verbal_components=True,
                         description="A creature of your choice that you can see within range regains hit points "
                                     "equal to 1d4 + your spellcasting ability modifier. This spell has no effect on "
                                     "undead or constructs.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the healing increases by 1d4 for each slot level above 1st.")


class HeatMetal(spells.Spell):
    """
    Heat Metal Spell
    SRD p. 153-154
    """

    def __init__(self):
        super().__init__(name="Heat Metal",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a piece of iron and a flame",
                         concentration=True,
                         duration="1 minute",
                         description="Choose a manufactured metal object, such as a metal weapon or a suit of heavy "
                                     "or medium metal armor, that you can see within range. You cause the object to "
                                     "glow red-hot. Any creature in physical contact with the object takes 2d8 fire "
                                     "damage when you cast the spell. Until the spell ends, you can use a bonus "
                                     "action on each of your subsequent turns to cause this damage again.\n"
                                     "If a creature is holding or wearing the object and takes the damage from it, "
                                     "the creature must succeed on a Constitution saving throw or drop the object if "
                                     "it can. If it doesn't drop the object, it has disadvantage on attack rolls and "
                                     "ability checks until the start of your next turn.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 2nd.")


class HuntersMark(spells.Spell):
    """
    Hunter's Mark Spell
    SRD p. 155
    """

    def __init__(self):
        super().__init__(name="Hunter's Mark",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         casting_time="1 bonus action",
                         school=SpellSchools.DIVINATION,
                         spell_range="90 feet",
                         verbal_components=True,
                         concentration=True,
                         duration="1 hour",
                         description="You choose a creature you can see within range and mystically mark it as your "
                                     "quarry. Until the spell ends, you deal an extra 1d6 damage to the target "
                                     "whenever you hit it with a weapon attack, and you have advantage on any Wisdom "
                                     "(Perception) or Wisdom (Survival) check you make to find it. If the target "
                                     "drops to 0 hit points before this spell ends, you can use a bonus action on a "
                                     "subsequent turn of yours to mark a new creature.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd or 4th level, you can "
                                          "maintain your concentration on the spell for up to 8 hours. When you use a "
                                          "spell slot of 5th level or higher, you can maintain your concentration on "
                                          "the spell for up to 24 hours.")


class Jump(spells.Spell):
    """
    Jump Spell
    SRD p. 158
    """

    def __init__(self):
        super().__init__(name="Jump",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a grasshopper's hind leg",
                         duration="1 minute",
                         description="You touch a creature. The creature's jump distance is tripled until the spell "
                                     "ends.")


class LesserRestoration(spells.Spell):
    """
    Lesser Restoration Spell
    SRD p. 158
    """

    def __init__(self):
        super().__init__(name="Lesser Restoration",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="You touch a creature and can end either one disease or one condition afflicting "
                                     "it. The condition can be blinded, deafened, paralyzed, or poisoned.")


class Light(spells.Spell):
    """
    Light Spell
    SRD p. 159
    """

    def __init__(self):
        super().__init__(name="Light",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.EVOCATION,
                         spell_range="Touch",
                         verbal_components=True,
                         material_components_list="a firefly or phosphorescent moss",
                         duration="1 hour",
                         description="You touch one object that is no larger than 10 feet in any dimension. Until the "
                                     "spell ends, the object sheds bright light in a 20-foot radius and dim light "
                                     "for an additional 20 feet. The light can be colored as you like. Completely "
                                     "covering the object with something opaque blocks the light. The spell ends if "
                                     "you cast it again or dismiss it as an action.\n"
                                     "If you target an object held or worn by a hostile creature, that creature must "
                                     "succeed on a Dexterity saving throw to avoid the spell.")


class LocateObject(spells.Spell):
    """
    Locate Object Spell
    SRD p. 159-160
    """

    def __init__(self):
        super().__init__(name="Locate Object",
                         spell_lists=[SpellLists.ARCANE,
                                      SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a forked twig",
                         concentration=True,
                         duration="10 minutes",
                         description="Describe or name an object that is familiar to you. You sense the direction to "
                                     "the object's location, as long as that object is within 1,000 feet of you. If "
                                     "the object is in motion, you know the direction of its movement.\n"
                                     "The spell can locate a specific object known to you, as long as you have seen "
                                     "it up close--within 30 feet--at least once. Alternatively, the spell can locate "
                                     "the nearest object of a particular kind, such as a certain kind of apparel, "
                                     "jewelry, furniture, tool, or weapon.\n"
                                     "This spell can't locate an object if any thickness of lead, even a thin sheet, "
                                     "blocks a direct path between you and the object.")


class Longstrider(spells.Spell):
    """
    Longstrider Spell
    SRD p. 160
    """

    def __init__(self):
        super().__init__(name="Longstrider",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a pinch of dirt",
                         duration="1 hour",
                         description="You touch a creature. The target's speed increases by 10 feet until the spell "
                                     "ends.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "you can target one additional creature for each slot level above 1st.")


class Mending(spells.Spell):
    """
    Mending Spell
    SRD p. 164
    """

    def __init__(self):
        super().__init__(name="Mending",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="two lodestones",
                         description="This spell repairs a single break or tear in an object you touch, such as a "
                                     "broken chain link, two halves of a broken key, a torn cloak, or a leaking "
                                     "wineskin. As long as the break or tear is no larger than 1 foot in any "
                                     "dimension, you mend it, leaving no trace of the former damage.\n"
                                     "This spell can physically repair a magic item or construct, but the spell can't "
                                     "restore magic to such an object.")


class Message(spells.Spell):
    """
    Message Spell
    SRD p. 164
    """

    def __init__(self):
        super().__init__(name="Message",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a short piece of copper wire",
                         duration="1 round",
                         description="You point your finger toward a creature within range and whisper a message. The "
                                     "target (and only the target) hears the message and can reply in a whisper that "
                                     "only you can hear.\n"
                                     "You can cast this spell through solid objects if you are familiar with the "
                                     "target and know it is beyond the barrier. Magical silence, 1 foot of stone, "
                                     "1 inch of common metal, a thin sheet of lead, or 3 feet of wood blocks the "
                                     "spell. The spell doesn't have to follow a straight line and can travel freely "
                                     "around corners or through openings.")


class PassWithoutTrace(spells.Spell):
    """
    Pas Without Trace Spell
    SRD p. 167
    """

    def __init__(self):
        super().__init__(name="Pass Without Trace",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="ashes from a burned leaf of mistletoe and a sprig of spruce",
                         concentration=True,
                         duration="1 hour",
                         description="A veil of shadows and silence radiates from you, masking you and your "
                                     "companions from detection. For the duration, each creature you choose within 30 "
                                     "feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and "
                                     "can't be tracked except by magical means. A creature that receives this bonus "
                                     "leaves behind no tracks or other traces of its passage.")


class PoisonSpray(spells.Spell):
    """
    Poison Spray Spell
    SRD p. 169
    """

    def __init__(self):
        super().__init__(name="Poison Spray",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.CONJURATION,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You extend your hand toward a creature you can see within range and project a "
                                     "puff of noxious gas from your palm. The creature must succeed on a Constitution "
                                     "saving throw or take 1d12 poison damage.\n"
                                     "This spell's damage increases by 1d12 when you reach 5th level (2d12), "
                                     "11th level (3d12), and 17th level (4d12).")


class ProtectionFromPoison(spells.Spell):
    """
    Protection From Poison Spell
    SRD p. 173
    """

    def __init__(self):
        super().__init__(name="Protection From Poison",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         duration="1 hour",
                         description="You touch a creature. If it is poisoned, you neutralize the poison. If more "
                                     "than one poison afflicts the target, you neutralize one poison that you know is "
                                     "present, or you neutralize one at random.\n"
                                     "For the duration, the target has advantage on saving throws against being "
                                     "poisoned, and it has resistance to poison damage.")


class PurifyFoodAndDrink(spells.Spell):
    """
    Purify Food and Drink Spell
    SRD p. 173
    """

    def __init__(self):
        super().__init__(name="Purify Food and Drink",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         ritual=True,
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="All nonmagical food and drink within a 5-foot-radius sphere centered on a point "
                                     "of your choice within range is purified and rendered free of poison and "
                                     "disease.")


class RayOfEnfeeblement(spells.Spell):
    """
    Ray of Enfeeblement Spell
    SRD p. 174
    """

    def __init__(self):
        super().__init__(name="Ray of Enfeeblement",
                         spell_lists=[SpellLists.ARCANE],
                         level=2,
                         school=SpellSchools.NECROMANCY,
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="A black beam of enervating energy springs from your finger toward a creature "
                                     "within range. Make a ranged spell attack against the target. On a hit, "
                                     "the target deals only half damage with weapon attacks that use Strength until "
                                     "the spell ends.\n"
                                     "At the end of each of the target's turns, it can make a Constitution saving "
                                     "throw against the spell. On a success, the spell ends.")


class Resistance(spells.Spell):
    """
    Resistance Spell
    SRD p. 175
    """

    def __init__(self):
        super().__init__(name="Resistance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a miniature cloak",
                         concentration=True,
                         duration="1 minute",
                         description="You touch one willing creature. Once before the spell ends, the target can roll "
                                     "a d4 and add the number rolled to one saving throw of its choice. It can roll "
                                     "the die before or after making the saving throw. The spell then ends.")


class Shillelagh(spells.Spell):
    """
    Shillelagh Spell
    SRD p. 179
    """

    def __init__(self):
        super().__init__(name="Shillelagh",
                         spell_lists=[SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         casting_time="1 bonus action",
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="(mistletoe, a shamrock leaf, and a club or quarterstaff",
                         duration="1 minute",
                         description="The wood of a club or quarterstaff you are holding is imbued with nature's "
                                     "power. For the duration, you can use your spellcasting ability instead of "
                                     "Strength for the attack and damage rolls of melee attacks using that weapon, "
                                     "and the weapon's damage die becomes a d8. The weapon also becomes magical, "
                                     "if it isn't already. The spell ends if you cast it again or if you let go of "
                                     "the weapon.")


class Silence(spells.Spell):
    """
    Silence Spell
    SRD p. 179
    """

    def __init__(self):
        super().__init__(name="Silence",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.ILLUSION,
                         ritual=True,
                         spell_range="120 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="10 minutes",
                         description="For the duration, no sound can be created within or pass through a "
                                     "20-foot-radius sphere centered on a point you choose within range. Any creature "
                                     "or object entirely inside the sphere is immune to thunder damage, and creatures "
                                     "are deafened while entirely inside it. Casting a spell that includes a verbal "
                                     "component is impossible there.")


class SpareTheDying(spells.Spell):
    """
    Spare the Dying Spell
    SRD p. 181
    """

    def __init__(self):
        super().__init__(name="Spare the Dying",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.NECROMANCY,
                         spell_range="Touch",
                         verbal_components=True,
                         somatic_components=True,
                         description="You touch a living creature that has 0 hit points. The creature becomes stable. "
                                     "This spell has no effect on undead or constructs.")


class SpeakWithAnimals(spells.Spell):
    """
    Speak with Animals Spell
    SRD p. 181
    """

    def __init__(self):
        super().__init__(name="Speak with Animals",
                         spell_lists=[SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.DIVINATION,
                         ritual=True,
                         spell_range="Self",
                         verbal_components=True,
                         somatic_components=True,
                         duration="10 minutes",
                         description="You gain the ability to comprehend and verbally communicate with beasts for the "
                                     "duration. The knowledge and awareness of many beasts is limited by their "
                                     "intelligence, but at minimum, beasts can give you information about nearby "
                                     "locations and monsters, including whatever they can perceive or have perceived "
                                     "within the past day. You might be able to persuade a beast to perform a small "
                                     "favor for you, at the GM's discretion.")


class SpikeGrowth(spells.Spell):
    """
    Spike Growth Spell
    SRD p. 182
    """

    def __init__(self):
        super().__init__(name="Spike Growth",
                         spell_lists=[SpellLists.PRIMAL],
                         level=2,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="150 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="seven sharp thorns or seven small twigs, each sharpened to a point",
                         concentration=True,
                         duration="10 minutes",
                         description="The ground in a 20-foot radius centered on a point within range twists and "
                                     "sprouts hard spikes and thorns. The area becomes difficult terrain for the "
                                     "duration. When a creature moves into or within the area, it takes 2d4 piercing "
                                     "damage for every 5 feet it travels.\n"
                                     "The transformation of the ground is camouflaged to look natural. Any creature "
                                     "that can't see the area at the time the spell is cast must make a Wisdom ("
                                     "Perception) check against your spell save DC to recognize the terrain as "
                                     "hazardous before entering it.")


class Thaumaturgy(spells.Spell):
    """
    Thaumaturgy Spell
    SRD p. 187
    """

    def __init__(self):
        super().__init__(name="Thaumaturgy",
                         spell_lists=[SpellLists.DIVINE],
                         level=0,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         duration="Up to 1 minute",
                         description="You manifest a minor wonder, a sign of supernatural power, within range. You "
                                     "create one of the following magical effects within range:\n"
                                     "• Your voice booms up to three times as loud as normal for 1 minute\n"
                                     "• You cause flames to flicker, brighten, dim, or change color for 1 minute.\n"
                                     "• You cause harmless tremors in the ground for 1 minute.\n"
                                     "• You create an instantaneous sound that originates from a point of your choice "
                                     "within range, such as a rumble of thunder, the cry of a raven, or ominous "
                                     "whispers.\n"
                                     "• You instantaneously cause an unlocked door or window to fly open or slam "
                                     "shut.\n"
                                     "• You alter the appearance of your eyes for 1 minute.\n"
                                     "If you cast this spell multiple times, you can have up to three of its 1-minute "
                                     "effects active at a time, and you can dismiss such an effect as an action.")


class Thunderwave(spells.Spell):
    """
    Thunderwave Spell
    SRD p. 187
    """

    def __init__(self):
        super().__init__(name="Thunderwave",
                         spell_lists=[SpellLists.ARCANE, SpellLists.PRIMAL],
                         level=1,
                         school=SpellSchools.TRANSMUTATION,
                         spell_range="Self (15-foot cube)",
                         verbal_components=True,
                         somatic_components=True,
                         description="A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube "
                                     "originating from you must make a Constitution saving throw. On a failed save, "
                                     "a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a "
                                     "successful save, the creature takes half as much damage and isn't pushed.\n"
                                     "In addition, unsecured objects that are completely within the area of effect "
                                     "are automatically pushed 10 feet away from you by the spell's effect, "
                                     "and the spell emits a thunderous boom audible out to 300 feet.",
                         at_higher_levels="When you cast this spell using a spell slot of 2nd level or higher, "
                                          "the damage increases by 1d8 for each slot level above 1st.")


class Dagger(weapons.Weapon):
    """
    Dagger Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Dagger",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.SIMPLE,
                         damage_dice="1d4",
                         damage_type=DamageTypes.PIERCING,
                         finesse=True,
                         light=True,
                         thrown=True,
                         attack_range=(20, 60),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Handaxe(weapons.Weapon):
    """
    Handaxe Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Handaxe",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.SIMPLE,
                         damage_dice="1d6",
                         damage_type=DamageTypes.SLASHING,
                         light=True,
                         thrown=True,
                         attack_range=(20, 60),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Boomerang(weapons.Weapon):
    """
    Boomerang Weapon
    SRD p. ??
    """

    def __init__(self,
                 name: str = "Boomerang",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.SIMPLE,
                         damage_dice="1d4",
                         damage_type=DamageTypes.BLUDGEONING,
                         thrown=True,
                         attack_range=(60, 120),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Maul(weapons.Weapon):
    """
    Maul Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Maul",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="2d6",
                         damage_type=DamageTypes.BLUDGEONING,
                         heavy=True,
                         two_handed=True,
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Rapier(weapons.Weapon):
    """
    Rapier Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Rapier",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d8",
                         damage_type=DamageTypes.PIERCING,
                         finesse=True,
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Shortsword(weapons.Weapon):
    """
    Shortsword Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Shortsword",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d6",
                         damage_type=DamageTypes.PIERCING,
                         finesse=True,
                         light=True,
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class HandCrossbow(weapons.Weapon):
    """
    Hand Crossbow Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Hand Crossbow",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d6",
                         damage_type=DamageTypes.PIERCING,
                         ammunition=True,
                         light=True,
                         loading=True,
                         attack_range=(30, 120),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


class Longbow(weapons.Weapon):
    """
    Longbow Weapon
    SRD p. 66
    """

    def __init__(self,
                 name: str = "Longbow",
                 magical: bool = False,
                 damage_bonus: int = 0,
                 attack_bonus: int = 0):
        super().__init__(name=name,
                         weapon_type=WeaponTypes.MARTIAL,
                         damage_dice="1d8",
                         damage_type=DamageTypes.PIERCING,
                         ammunition=True,
                         heavy=True,
                         two_handed=True,
                         attack_range=(150, 600),
                         magical=magical,
                         damage_bonus=damage_bonus,
                         attack_bonus=attack_bonus)


CONTENT = {
    "Armors": {
        "Padded": Padded,
        "Leather": Leather,
        "Studded Leather": StuddedLeather,
        "Hide": Hide,
        "Chain Shirt": ChainShirt,
        "Scale Mail": ScaleMail,
        "Breastplate": Breastplate,
        "Half Plate": HalfPlate,
        "Ring Mail": RingMail,
        "Chain Mail": ChainMail,
        "Splint": Splint,
        "Plate": Plate,
        "Shield": Shield,
    },
    "Classes": {
        # TODO The rest of the subclasses
        # "Berserker Barbarian": BerserkerBarbarian,
        "Lore Bard": "OBSOLETE",
        # "Life Cleric": LifeCleric,
        # "Land Druid": LandDruid,
        "Champion Fighter": ChampionFighter,
        # "Open Hand Monk": OpenHandMonk,
        # "Devotion Paladin": DevotionPaladin,
        "Hunter Ranger": "OBSOLETE",
        "Thief Rogue": "OBSOLETE",
        # "Draconic Sorcerer": DraconicSorcerer,
        # "Fiend Warlock": FiendWarlock,
        # "Evocation Wizard": EvocationWizard,
    },
    "Feats": {
        "Grappler": "OBSOLETE",
    },
    "Magic Items": {
        # TODO All Magic Items
    },
    "Races": {
        "Dwarf": "OBSOLETE",
        "High Elf": "OBSOLETE",
        "Halfling": "OBSOLETE",
        "Human": "OBSOLETE",
        "Black Dragonborn": "OBSOLETE",
        "Blue Dragonborn": "OBSOLETE",
        "Brass Dragonborn": "OBSOLETE",
        "Bronze Dragonborn": "OBSOLETE",
        "Copper Dragonborn": "OBSOLETE",
        "Gold Dragonborn": "OBSOLETE",
        "Green Dragonborn": "OBSOLETE",
        "Red Dragonborn": "OBSOLETE",
        "Silver Dragonborn": "OBSOLETE",
        "White Dragonborn": "OBSOLETE",
        "Rock Gnome": "OBSOLETE",
        "Half-Elf": "OBSOLETE",
        "Half-Orc": "OBSOLETE",
        "Infernal Tiefling": "OBSOLETE",
    },
    "Spells": {
        # TODO The rest of the spells
        # "Acid Arrow": AcidArrow,
        # "Acid Splash": AcidSplash,
        # "Aid": Aid,
        # "Alarm": Alarm,
        # "Alter Self", AlterSelf,
        "Animal Friendship": AnimalFriendship,
        "Animal Messenger": AnimalMessenger,
        # "Animal Shapes": AnimalShapes,
        # "Animate Dead": AnimateDead,
        # "Animate Objects": AnimateObjects,
        # "Antilife Shell": AntilifeShell,
        # "Antimagic Field": AntimagicField,
        # "Antipathy/Sympathy": AntipathySympathy,
        # "Arcane Eye": ArcaneEye,
        # "Arcane Hand": ArcaneHand,
        # "Arcane Lock": ArcaneLock,
        # "Arcane Sword": ArcaneSword,
        # "Arcanist's Magic Aura": ArcanistsMagicAura,
        # "Astral Projection": AstralProjection,
        "Augury": Augury,
        # "Awaken": Awaken,
        # "Bane": Bane,
        # "Banishment": Banishment,
        "Barkskin": "OBSOLETE",
        # "Beacon of Hope": BeaconOfHope,
        # "Bestow Curse": BestowCurse,
        # "Black Tentacles": BlackTentacles,
        # "Blade Barrier": BladeBarrier,
        # "Bless": Bless,
        # "Blight": Blight,
        # "Blindness/Deafness": BlindnessDeafness,
        # "Blink": Blink,
        # "Blur": Blur,
        # "Branding Smite": BrandingSmite,
        # "Burning Hands": BurningHands,
        # "Call Lightning": CallLightning,
        # "Calm Emotions": CalmEmotions,
        # "Chain Lightning": ChainLightning,
        # "Charm Person": CharmPerson,
        "Chill Touch": ChillTouch,
        # "Circle of Death": CircleOfDeath,
        # "Clairvoyance": Clairvoyance,
        # "Clone": Clone,
        # "Cloudkill": Cloudkill,
        # "Color Spray": ColorSpray,
        # "Command": Command,
        # "Commune": Commune,
        # "Commune with Nature": CommuneWithNature,
        # "Comprehend Languages": ComprehendLanguages,
        # "Compulsion": Compulsion,
        # "Cone of Cold": ConeOfCold,
        # "Confusion": Confusion,
        # "Conjure Animals": ConjureAnimals,
        # "Conjure Celestial": ConjureCelestial,
        # "Conjure Elemental": ConjureElemental,
        # "Conjure Fey": ConjureFey,
        # "Conjure Minor Elementals": ConjureMinorElementals,
        # "Conjure Woodland Beings": ConjureWoodlandBeings,
        # "Contact Other Plane": ConjureOtherPlane,
        # "Contagion": Contagion,
        # "Contingency": Contingency,
        # "Continual Flame": ContinualFlame,
        # "Control Water": ControlWater,
        # "Control Weather": ControlWeather,
        # "Counterspell": Counterspell,
        # "Create Food and Water": CreateFoodAndWater,
        "Create or Destroy Water": CreateOrDestroyWater,
        # "Create Undead": CreateUndead,
        # "Creation": Creation,
        "Cure Wounds": CureWounds,
        # "Dancing Lights": DancingLights,
        # "Darkness": Darkness,
        "Darkvision": Darkvision,
        # "Daylight": Daylight,
        # "Death Ward": DeathWard,
        # "Delayed Blast Fireball": DelayedBlastFireball,
        # "Demiplane": Demiplane,
        # "Detect Evil and Good": DetectEvilAndGood,
        "Detect Magic": DetectMagic,
        "Detect Poison and Disease": DetectPoisonAndDisease,
        "Detect Thoughts": DetectThoughts,
        # "Dimension Door": DimensionDoor,
        # "Disguise Self": DisguiseSelf,
        # "Disintegrate": Disintegrate,
        # "Dispel Evil and Good": DispelEvilAndGood,
        # "Dispel Magic": DispelMagic,
        # "Divination": Divination,
        # "Divine Favor": DivineFavor,
        # "Divine Word": DivineWord,
        # "Dominate Beast": DominateBeast,
        # "Dominate Monster": DominateMonster,
        # "Dominate Person": DominatePerson,
        # "Dream": Dream,
        "Druidcraft": Druidcraft,
        # "Earthquake": Earthquake,
        # "Eldritch Blast": EldritchBlast,
        "Enhance Ability": EnhanceAbility,
        "Enlarge/Reduce": EnlargeReduce,
        "Entangle": Entangle,
        # "Enthrall": Enthrall,
        # "Etherealness": Etherealness,
        # "Expeditious Retreat": ExpeditiousRetreat,
        # "Eyebite": Eyebite,
        # "Fabricate": Fabricate,
        # "Faerie Fire": FaerieFire,
        # "Faithful Hound": FaithfulHound,
        "False Life": FalseLife,
        # "Fear": Fear,
        # "Feather Fall": FeatherFall,
        # "Feeblemind": Feeblemind,
        # "Find Familiar": FindFamiliar,
        # "Find Steed": FindSteed,
        # "Find the Path": FindThePath,
        "Find Traps": FindTraps,
        # "Finger of Death": FingerOfDeath,
        # "Fireball": Fireball,
        # "Fire Bolt": FireBolt,
        # "Fire Shield": FireShield,
        # "Fire Storm": FireStorm,
        # "Flame Blade": FlameBlade,
        # "Flame Strike": FlameStrike,
        # "Flaming Sphere": FlamingSphere,
        # "Flesh to Stone": FleshToStone,
        # "Floating Disk": FloatingDisk,
        # "Fly": Fly,
        "Fog Cloud": FogCloud,
        # "Forbiddance": Forbiddance,
        # "Forcecage": Forcecage,
        # "Foresight": Foresight,
        # "Freedom of Movement": FreedomOfMovement,
        # "Freezing Sphere": FreezingSphere,
        # "Gaseous Form": GaseousForm,
        # "Gate": Gate,
        # "Geas": Geas,
        "Gentle Repose": GentleRepose,
        # "Giant Insect": GiantInsect,
        # "Glibness": Glibness,
        # "Globe of Invulnerability": GlobeOfInvulnerability,
        # "Glyph of Warning": GlyphOfWarning,
        "Goodberry": Goodberry,
        # "Grease": Grease,
        # "Greater Invisibility": GreaterInvisibility,
        # "Greater Restoration": GreaterRestoration,
        # "Guardian of Faith": GuardianOfFaith,
        # "Guards and Wards": GuardsAndWards,
        "Guidance": "OBSOLETE",
        # "Guiding Bolt": GuidingBolt,
        # "Gust of Wind": GustOfWind,
        # "Hallow": Hallow,
        # "Hallucinatory Terrain": HallucinatoryTerrain,
        # "Harm": Harm,
        # "Haste": Haste,
        # "Heal": Heal,
        "Healing Word": HealingWord,
        "Heat Metal": HeatMetal,
        # "Hellish Rebuke": HellishRebuke,
        # "Heroes' Feast": HeroesFeast,
        # "Heroism": Heroism,
        # "Hideous Laughter": HideousLaughter,
        # "Hold Monster": HoldMonster,
        # "Hold Person": HoldPerson,
        # "Holy Aura": HolyAura,
        "Hunter's Mark": HuntersMark,
        # "Hypnotic Pattern": HypnoticPattern,
        # "Ice Storm": IceStorm,
        # "Identify": Identify,
        # "Illusory Script": IllusoryScript,
        # "Imprisonment": Imprisonment,
        # "Incendiary Cloud": IncendiaryCloud,
        # "Inflict Wounds": InflictWounds,
        # "Insect Plague": InsectPlague,
        # "Instant Summons": InstantSummons,
        # "Invisibility": Invisibility,
        # "Irresistible Dance": IrresistibleDance,
        "Jump": Jump,
        # "Knock": Knock,
        # "Legend Lore": LegendLore,
        "Lesser Restoration": LesserRestoration,
        # "Levitate": Levitate,
        "Light": Light,
        # "Lightning Bolt": LightningBolt,
        # "Locate Animals or Plants": LocateAnimalsOrPlants,
        # "Locate Creature": LocateCreature,
        "Locate Object": LocateObject,
        "Longstrider": Longstrider,
        # "Mage Armor": MageArmor,
        # "Mage Hand": MageHand,
        # "Magic Circle": MagicCircle,
        # "Magic Jar": MagicJar,
        # "Magic Missile": MagicMissile,
        # "Magic Mouth": MagicMouth,
        # "Magic Weapon": MagicWeapon,
        # "Magnificent Mansion": MagnificentMansion,
        # "Major Image": MajorImage,
        # "Mass Cure Wounds": MassCureWounds,
        # "Mass Heal": MassHeal,
        # "Mass Healing Word": MassHealingWord,
        # "Mass Suggestion": MassSuggestion,
        # "Maze": Maze,
        # "Meld into Stone": MeldIntoStone,
        "Mending": Mending,
        "Message": Message,
        # "Meteor Swarm": MeteorSwarm,
        # "Mind Blank": MindBlank,
        # "Minor Illusion": MinorIllusion,
        # "Mirage Arcane": MirageArcane,
        # "Mirror Image": MirrorImage,
        # "Mislead": Mislead,
        # "Misty Step": MistyStep,
        # "Modify Memory": ModifyMemory,
        # "Moonbeam": Moonbeam,
        # "Move Earth": MoveEarth,
        # "Nondetection": Nondetection,
        "Pass Without Trace": PassWithoutTrace,
        # "Passwall": Passwall,
        # "Phantasmal Killer": PhantasmalKiller,
        # "Phantom Steed": PhantomSteed,
        # "Planar Ally": PlanarAlly,
        # "Planar Binding": PlanarBinding,
        # "Plane Shift": PlaneShift,
        # "Plant Growth": PlantGrowth,
        "Poison Spray": PoisonSpray,
        # "Polymorph": Polymorph,
        # "Power Word Kill": PowerWordKill,
        # "Power Word Stun": PowerWordStun,
        # "Prayer of Healing": PrayerOfHealing,
        # "Prestidigitation": Prestidigitation,
        # "Prismatic Spray": PrismaticSpray,
        # "Prismatic Wall": PrismaticWall,
        # "Private Sanctum": PrivateSanctum,
        # "Produce Flame": ProduceFlame,
        # "Programmed Illusion": ProgrammedIllusion,
        # "Project Image": ProjectImage,
        # "Protection from Energy": ProtectionFromEnergy,
        # "Protection from Good and Evil": ProtectionFromGoodAndEvil,
        "Protection from Poison": ProtectionFromPoison,
        "Purify Food and Drink": PurifyFoodAndDrink,
        # "Raise Dead": RaiseDead,
        "Ray of Enfeeblement": RayOfEnfeeblement,
        # "Ray of Frost": RayOfFrost,
        # "Regenerate": Regenerate,
        # "Reincarnate": Reincarnate,
        # "Remove Curse": RemoveCurse,
        # "Resilient Sphere": ResilientSphere,
        "Resistance": Resistance,
        # "Resurrection": Resurrection,
        # "Reverse Gravity": ReverseGravity,
        # "Revivify": Revivify,
        # "Rope Trick": RopeTrick,
        # "Sacred Flame": SacredFlame,
        # "Sanctuary": Sanctuary,
        # "Scorching Ray": ScorchingRay,
        # "Scrying": Scrying,
        # "Secret Chest": SecretChest,
        # "See Invisibility": SeeInvisibility,
        # "Seeming": Seeming,
        # "Sending": Sending,
        # "Sequester": Sequester,
        # "Shapechange": Shapechange,
        # "Shatter": Shatter,
        # "Shield": ShieldSpell,
        # "Shield of Faith": ShieldOfFaith,
        "Shillelagh": Shillelagh,
        # "ShockingGrasp": ShockingGrasp,
        "Silence": Silence,
        # "Silent Image": SilentImage,
        # "Simulacrum": Simulacrum,
        # "Sleep": Sleep,
        # "Sleet Storm": SleetStorm,
        # "Slow": Slow,
        "Spare the Dying": SpareTheDying,
        "Speak with Animals": SpeakWithAnimals,
        # "Speak with Dead": SpeakWithDead,
        # "Speak with Plants": SpeakWithPlants,
        # "Spider Climb": SpiderClimb,
        "Spike Growth": SpikeGrowth,
        # "Spirit Guardians": SpiritGuardians,
        # "Spiritual Weapon": SpiritualWeapon,
        # "Stinking Cloud": StinkingCloud,
        # "Stone Shape": StoneShape,
        # "Stoneskin": Stoneskin,
        # "Storm of Vengeance": StormOfVengeance,
        # "Suggestion": Suggestion,
        # "Sunbeam": Sunbeam,
        # "Sunburst": Sunburst,
        # "Symbol": Symbol,
        # "Telekinesis": Telekinesis,
        # "Telepathic Bond": TelepathicBond,
        # "Teleport": Teleport,
        # "Teleportation Circle": TeleportationCircle,
        "Thaumaturgy": Thaumaturgy,
        "Thunderwave": Thunderwave,
        # "Time Stop": TimeStop,
        # "Tiny Hut": TinyHut,
        # "Tongues": Tongues,
        # "Transport via Plants": TransportViaPlants,
        # "Tree Stride": TreeStride,
        # "True Polymorph": TruePolymorph,
        # "True Resurrection": TrueResurrection,
        # "True Seeing": TrueSeeing,
        # "True Strike": TrueStrike,
        # "Unseen Servant": UnseenServant,
        # "Vampiric Touch": VampiricTouch,
        # "Vicious Mockery": ViciousMockery,
        # "Wall of Fire": WallOfFire,
        # "Wall of Force": WallOfForce,
        # "Wall of Ice": WallOfIce,
        # "Wall of Stone": WallOfStone,
        # "Wall of Thorns": WallOfThorns,
        # "Warding Bond": WardingBond,
        # "Water Breathing": WaterBreathing,
        # "Water Walk": WaterWalk,
        # "Web": Web,
        # "Weird": Weird,
        # "Wind Walk": WindWalk,
        # "Wind Wall": WindWall,
        # "Wish": Wish,
        # "Word of Recall": WordOfRecall,
        # "Zone of Truth": ZoneOfTruth,
    },
    "Weapons": {
        # TODO The rest of the weapons
        # "Club": Club,
        "Dagger": Dagger,
        # "Greatclub": Greatclub,
        "Handaxe": Handaxe,
        # "Javelin": Javelin,
        # "Light Hammer": LightHammer,
        # "Mace": Mace,
        # "Quarterstaff": Quarterstaff,
        # "Sickle": Sickle,
        # "Spear": Spear,
        # "Light Crossbow": LightCrossbow,
        # "Dart": Dart,
        # "Shortbow": Shortbow,
        # "Sling": Sling,
        "Boomerang": Boomerang,
        # "Battleaxe": Battleaxe,
        # "Flail": Flail,
        # "Glaive": Glaive,
        # "Greataxe": Greataxe,
        # "Greatsword": Greatsword,
        # "Halberd": Halberd,
        # "Lance": Lance,
        # "Longsword": Longsword,
        "Maul": Maul,
        # "Morningstar": Morningstar,
        # "Pike": Pike,
        "Rapier": Rapier,
        # "Scimitar": Scimitar,
        "Shortsword": Shortsword,
        # "Trident": Trident,
        # "War Pick": WarPick,
        # "Warhammer": Warhammer,
        # "Whip": Whip,
        # "Blowgun": Blowgun,
        "Hand Crossbow": HandCrossbow,
        # "Heavy Crossbow": HeavyCrossbow,
        "Longbow": Longbow,
        # "Net": Net
    },
}
