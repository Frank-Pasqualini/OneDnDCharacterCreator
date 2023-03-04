"""
Content from the Dungeons and Dragons OneD&D Character Origins Unearthed Arcana.
https://media.dndbeyond.com/compendium-images/one-dnd/cleric-and-revised-species/tr8jAj5cc33uQixi/UA-2022-ClericandSpecies.pdf
"""

from rules import abilities, bonuses, classes, feats, species, spells
from rules.enums import AbilityNames, ArmorTraining, DamageTypes, ProficiencyLevels, Skills, SpellSchools, SpellLists
from rules.enums import WeaponTypes


class LifeCleric(classes.Cleric):
    """
    Life subclass for Cleric
    SRD p. 25
    """

    def __init__(self, **kwargs):
        super().__init__(name="Life Cleric", **kwargs)

    def _level_up_3(self, content: dict[str, dict[str, any]]):
        self._features.append(feats.Feat(name="Domain Spells",
                                         description="Your connection to this divine domain ensures you always have "
                                                     "certain Spells ready. When you reach a Cleric level specified "
                                                     "in the Life Domain Spells table, you thereafter always have the "
                                                     "listed Spells prepared. These Spells don't count against the "
                                                     "number of Spells you can prepare, and they follow the rules of "
                                                     "this Class's Spellcasting feature.",
                                         feat_spells=[
                                             content["Spells"]["Lesser Restoration"](
                                             ),
                                             content["Spells"]["Prayer of Healing"](
                                             ),
                                             content["Spells"]["Mass Healing Word"](
                                             ),
                                             content["Spells"]["Revivify"](),
                                             content["Spells"]["Aura of Life"](),
                                             content["Spells"]["Death Ward"](),
                                             content["Spells"]["Greater Restoration"](
                                             ),
                                             content["Spells"]["Mass Cure Wounds"](),
                                         ],
                                         spellcasting_ability=AbilityNames.WISDOM,
                                         visible=False))
        self._features.append(feats.Feat(name="Disciple of Life",
                                         description="Your healing Spells are empowered by life itself. When a Spell "
                                                     "you cast with a Spell Slot restores Hit Points to a creature, "
                                                     "that creature regains additional Hit Points on the turn you "
                                                     "cast the Spell. The additional Hit Points equal 2 plus the "
                                                     "Spell's level."))

    def _level_up_6(self):
        self._features.append(feats.Feat(name="Preserve Life",
                                         description="You can use your Channel Divinity to heal a group of the "
                                                     "critically injured. As an Action, you expend one use of your "
                                                     "Channel Divinity and present your Holy Symbol, restoring a "
                                                     "number of Hit Points equal to 5 times your Cleric level. Choose "
                                                     "any creatures within 30 feet of yourself (you can choose "
                                                     "yourself), and divide those Hit Points among the chosen "
                                                     "creatures. This feature can bring a creature's current Hit "
                                                     "Points to no more than half its Hit Point Maximum."))

    def _level_up_10(self):
        self._features.append(feats.Feat(name="Blessed Healer",
                                         description="The healing spells you cast on others heal you as well. When "
                                                     "you cast a spell with a Spell Slot on another creature that "
                                                     "restores Hit Points to it, you regain Hit Points equal to 2 "
                                                     "plus the Spell's level on the turn you cast the Spell."))

    def _level_up_14(self):
        self._features.append(feats.Feat(name="Supreme Healing",
                                         description="When you would normally roll one or more dice to restore Hit "
                                                     "Points to a creature with a Spell that you cast with a Spell "
                                                     "Slot, don't roll those dice for the healing; instead use the "
                                                     "highest number possible for each die. For example, instead of "
                                                     "restoring 2d6 Hit Points to a creature with a Spell, "
                                                     "you restore 12."))


class AbilityScoreImprovement(feats.Feat):
    """
    Ability Score Improvement Feat
    UA p. 11
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


class HolyOrderProtector(feats.HolyOrder):
    """
    Holy Order Protector
    """

    def __init__(self):
        super().__init__(name="Holy Order: Protector",
                         description="Trained for battle, you gain Martial Weapon Proficiency and Heavy Armor "
                                     "Training.",
                         feat_bonuses=bonuses.Bonuses(weapon_types=[WeaponTypes.MARTIAL],
                                                      armor_training=[ArmorTraining.HEAVY]),
                         visible=False)


class HolyOrderScholar(feats.HolyOrder):
    """
    Holy Order Scholar
    """

    def __init__(self, skill1: Skills, skill2: Skills):
        allowable_skills = [Skills.ARCANA, Skills.HISTORY,
                            Skills.NATURE, Skills.PERSUASION, Skills.RELIGION]

        if (skill1 not in allowable_skills) or (skill2 not in allowable_skills):
            raise Exception("All skills must be in the approved skill list")

        if skill1 == skill2:
            raise Exception("Both skills must be unique")

        super().__init__(name="*** Holy Order: Scholar",
                         description="Studying and teaching about lore of the gods and the multiverse, you gain "
                                     f"Proficiency in {skill1.value} and {skill2.value}. Whenever you make an Ability "
                                     "Check using either Skill, you gain a bonus to the check equal to your Wisdom "
                                     "Modifier.",  # TODO add modifier
                         feat_bonuses=bonuses.Bonuses(skills={skill1: ProficiencyLevels.PROFICIENT,
                                                              skill2: ProficiencyLevels.PROFICIENT}))


class HolyOrderThaumaturge(feats.HolyOrder):
    """
    Holy Order Thaumaturge
    """

    def __init__(self):
        super().__init__(name="Holy Order: Thaumaturge",
                         description="Delving deeper into your divine magical abilities, you can prepare one extra "
                                     "0-level Spell from the Divine Spell list. In addition, you regain one expended "
                                     "use of your Channel Divinity whenever you finish a Short Rest.")


class Dragonborn(species.Species):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self,
                 name: str,
                 ancestry: feats.Feat,
                 damage_type: DamageTypes):
        super().__init__(name=name,
                         features=[
                             ancestry,
                             feats.Feat(
                                 name="Breath Weapon",
                                 description="When you take the Attack Action on your turn, you can replace one of "
                                             "your attacks with an exhalation of magical energy in either a 15-foot "
                                             "cone or a 30-foot line that is 5 feet wide. Each creature in that area "
                                             "must make a Dexterity Saving Throw against a DC equal to 8 + your "
                                             "Constitution modifier + your Proficiency Bonus. On a failed save, "
                                             f"a creature takes 1d10 {damage_type.value} damage. On a successful save, "
                                             "a creature takes half as much damage. This damage increases by 1d10 "
                                             "when you reach the following character levels: 5th level (2d10), "
                                             "11th level (3d10), and 17th level (4d10).\n"
                                             "You can use this Breath Weapon a number of times equal to your "
                                             "Proficiency Bonus, and you regain all expended uses when you finish a "
                                             "Long Rest."
                             ),
                             feats.Feat(
                                 name="Damage Resistance",
                                 description=f"You have Resistance to {damage_type.value} damage."
                             ),
                             feats.Feat(
                                 name="Darkvision",
                                 description="You have Darkvision with a range of 60 feet."
                             ),
                             feats.Feat(
                                 name="Draconic Flight",
                                 description="When you reach 5th level, you learn how to channel the magical energy "
                                             "of your Draconic Ancestry to give yourself temporary flight. As a Bonus "
                                             "Action, you sprout spectral wings on your back that last for 10 minutes "
                                             "or until you are Incapacitated or you retract the wings as a Bonus "
                                             "Action. During that time, you have a Fly Speed equal to your Speed. "
                                             "Your wings appear to be made of the energy used by your Breath Weapon. "
                                             "Once you use this trait, you can't use it again until you finish a Long "
                                             "Rest.",
                             )
                         ],
                         life_span=80)


class BlackDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Black Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Black Dragon progenitor.",
                             visible=False
                         ),
                         damage_type=DamageTypes.ACID)


class BlueDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Blue Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Blue Dragon progenitor.",
                             visible=False
                         ),
                         damage_type=DamageTypes.LIGHTNING)


class BrassDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Brass Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Brass Dragon progenitor.",
                             visible=False
                         ),
                         damage_type=DamageTypes.FIRE)


class BronzeDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Bronze Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Bronze Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.LIGHTNING)


class CopperDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Copper Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Copper Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.ACID)


class GoldDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Gold Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Gold Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.FIRE)


class GreenDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Green Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Green Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.POISON)


class RedDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Red Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Red Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.FIRE)


class SilverDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="Silver Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a Silver Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.COLD)


class WhiteDragonborn(Dragonborn):
    """
    Dragonborn Species
    UA p. 9
    """

    def __init__(self):
        super().__init__(name="White Dragonborn",
                         ancestry=feats.Feat(
                             name="Draconic Ancestry",
                             description="Your lineage stems from a White Dragon progenitor.",
                             visible=False,
                         ),
                         damage_type=DamageTypes.COLD)


class Goliath(species.Species):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self,
                 name: str,
                 ancestry: feats.Feat):
        super().__init__(name=name,
                         features=[
                             ancestry,
                             feats.Feat(
                                 name="Large Form",
                                 description="Starting at 5th level, you gain the ability to supernaturally grow. As "
                                             "a Bonus Action, you change your Size to Large, provided you're in a big "
                                             "enough space. This transformation lasts for 10 minutes or until you end "
                                             "it as a Bonus Action. During that duration, you have Advantage on "
                                             "Strength Checks, and your Speed increases by 10 feet. Once you use this "
                                             "trait, you can't use it again until you finish a Long Rest. "
                             ),
                             feats.Feat(
                                 name="Powerful Build",
                                 description="You have Advantage on any Saving Throw you make to end the Grappled "
                                             "condition on yourself. You also count as one Size larger when "
                                             "determining your carrying capacity and the weight you can push, drag, "
                                             "or lift. "
                             ),
                         ],
                         speed=35,
                         life_span=80)


class CloudGoliath(Goliath):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self):
        super().__init__(name="Cloud Goliath",
                         ancestry=feats.Feat(
                             name="Cloud's Jaunt",
                             description="You are descended from Cloud Giants. As a Bonus Action, you magically "
                                         "Teleport up to 30 feet to an unoccupied space you can see. You can do this "
                                         "a number of times equal to your Proficiency Bonus, and you regain all "
                                         "expended uses when you finish a Long Rest."))


class FireGoliath(Goliath):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self):
        super().__init__(name="Fire Goliath",
                         ancestry=feats.Feat(
                             name="Fire's Burn",
                             description="You are descended from Fire Giants. When you hit a target with an Attack "
                                         "Roll and deal damage to it, you can also deal 1d10 Fire Damage to that "
                                         "target. You can do this a number of times equal to your Proficiency Bonus, "
                                         "and you regain all expended uses when you finish a Long Rest."))


class FrostGoliath(Goliath):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self):
        super().__init__(name="Frost Goliath",
                         ancestry=feats.Feat(
                             name="Frost's Chill",
                             description="You are descended from Frost Giants. When you hit a target with an Attack "
                                         "Roll and deal damage to it, you can also deal 1d6 Cold Damage to that "
                                         "target and reduce its Speed by 10 feet until the start of your next turn. "
                                         "You can do this a number of times equal to your Proficiency Bonus, "
                                         "and you regain all expended uses when you finish a Long Rest."))


class HillGoliath(Goliath):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self):
        super().__init__(name="Hill Goliath",
                         ancestry=feats.Feat(
                             name="Hill's Tumble",
                             description="You are descended from Hill Giants. When you hit a Large or smaller "
                                         "creature with an Attack Roll and deal damage to it,you can knock that "
                                         "target Prone. You can do this a number of times equal to your Proficiency "
                                         "Bonus, and you regain all expended uses when you finish a Long Rest."))


class StoneGoliath(Goliath):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self):
        super().__init__(name="Stone Goliath",
                         ancestry=feats.Feat(
                             name="Stone's Endurance",
                             description="You are descended from Stone Giants. When you take damage,you can use your "
                                         "Reaction to roll a d12. Add your Constitution modifier to the number rolled "
                                         "and reduce the damage by that total. You can do this a number of times "
                                         "equal to your Proficiency Bonus, and you regain all expended uses when you "
                                         "finish a Long Rest."))


class StormGoliath(Goliath):
    """
    Goliath Species
    UA p. 9-10
    """

    def __init__(self):
        super().__init__(name="Storm Goliath",
                         ancestry=feats.Feat(
                             name="Storm's Thunder",
                             description="You are descended from Storm Giants. When you take damage from a creature "
                                         "within 60 feet of you, you can use your Reaction to deal 1d8 Thunder Damage "
                                         "to that creature. You can do this a number of times equal to your "
                                         "Proficiency Bonus, and you regain all expended uses when you finish a Long "
                                         "Rest."))


class Aid(spells.Spell):
    """
    Aid Spell
    UA p. 12
    """

    def __init__(self):
        super().__init__(name="Aid",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="a tiny strip of white cloth",
                         description="Your spell bolsters creatures, filling them with resolve. Choose up to six "
                                     "creatures within range. Each target gains 5 Temporary Hit Points.",
                         at_higher_levels="When you cast this spell using a spell slot of 3rd level or higher, the "
                                          "number of Temporary Hit Points increases by 5 for each slot level above "
                                          "2nd.")


class Banishment(spells.Spell):
    """
    Banishment Spell
    UA p. 15-16
    """

    def __init__(self):
        super().__init__(name="Banishment",
                         spell_lists=[SpellLists.ARCANE, SpellLists.DIVINE],
                         level=4,
                         school=SpellSchools.CONJURATION,
                         spell_range="30 feet",
                         verbal_components=True,
                         somatic_components=True,
                         material_components_list="an item distasteful to the target",
                         concentration=True,
                         duration="1 minute",
                         description="You attempt to send one creature that you can see within range to another plane "
                                     "of existence. The target must succeed on a Charisma Saving Throw or be "
                                     "transported to a harmless demiplane for the duration. The target can willingly "
                                     "fail the save.\n"
                                     "While in the demiplane, the target is Incapacitated. At the end of each of its "
                                     "turns, the target can repeat the save, ending the Spell on itself on a success. "
                                     "When the Spell ends on the target, it reappears in the space it left or in the "
                                     "nearest unoccupied space if that space is occupied.\n"
                                     "If the Spell lasts on the target for 1 minute and the target is an Aberration, "
                                     "a Celestial, an Elemental, a Fey, or a Fiend, the target doesn't return. It is "
                                     "instead transported to a random location on a plane associated with its "
                                     "Creature Type.",
                         at_higher_levels="When you cast this Spell using a Spell Slot of 5th level or higher, you can "
                                          "target one additional creature for each slot level above 4th.")


class Guidance(spells.Spell):
    """
    Guidance Spell
    UA p. 19
    """

    def __init__(self):
        super().__init__(name="Guidance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.DIVINATION,
                         casting_time="Reaction, which you take in response to you or an ally within 10 feet of you "
                                      "failing an Ability Check",
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You channel magical insight to the creature who failed the Ability Check. That "
                                     "creature can roll a d4 and add the number rolled to the check, potentially "
                                     "turning it into a success.")


class PrayerOfHealing(spells.Spell):
    """
    Prayer of Healing Spell
    UA p. 23
    """

    def __init__(self):
        super().__init__(name="Prayer of Healing",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.ABJURATION,
                         casting_time="10 minutes",
                         spell_range="30 feet",
                         verbal_components=True,
                         description="You utter an extended prayer of restoration. Choose a number of willing "
                                     "creatures equal to your Spellcasting Ability Modifier (minimum of 1). Each of "
                                     "those creatures who remains within range for the Spell's entire casting gains "
                                     "the benefits of a Short Rest and also regains 2d8 Hit Points, and a creature "
                                     "can't be affected by this Spell again until that creature finishes a Long Rest.",
                         at_higher_levels="When you cast this Spell using a Spell Slot of 3rd level or higher, the "
                                          "healing increases by 1d8 for each slot above 2nd.")


class Resistance(spells.Spell):
    """
    Resistance Spell
    UA p. 25
    """

    def __init__(self):
        super().__init__(name="Resistance",
                         spell_lists=[SpellLists.DIVINE, SpellLists.PRIMAL],
                         level=0,
                         school=SpellSchools.ABJURATION,
                         casting_time="Reaction, which you take in response to you or an ally within 10 feet of you "
                                      "failing a Saving Throw",
                         spell_range="10 feet",
                         verbal_components=True,
                         somatic_components=True,
                         description="You channel magical protection to the creature who failed the Saving Throw. That "
                                     "creature can roll a d4 and add the number rolled to the save, potentially "
                                     "turning it into a success.")


class SpiritualWeapon(spells.Spell):
    """
    Spiritual Weapon Spell
    UA p. 25
    """

    def __init__(self):
        super().__init__(name="Spiritual Weapon",
                         spell_lists=[SpellLists.DIVINE],
                         level=2,
                         school=SpellSchools.EVOCATION,
                         casting_time="Bonus Action",
                         spell_range="60 feet",
                         verbal_components=True,
                         somatic_components=True,
                         concentration=True,
                         duration="1 minute",
                         description="You create a floating, spectral force that resembles a weapon of your choice "
                                     "and that lasts for the duration. The force appears within range in a space of "
                                     "your choice, and you can immediately make one melee spell attack against a "
                                     "creature within 5 feet of the force. On a hit, the target takes Force Damage "
                                     "equal to 1d8 + your spellcasting ability modifier.\n"
                                     "As a Bonus Action on your later turns, you can move the force up to 20 feet and "
                                     "repeat the attack against a creature within 5 feet of it.",
                         at_higher_levels="When you cast this Spell using a Spell Slot of 3rd level or higher, the "
                                          "damage increases by 1d8 for every slot level above 2nd.")


CONTENT = {
    "Classes": {
        "Life Cleric": LifeCleric,
    },
    "Feats": {
        "Ability Score Improvement": AbilityScoreImprovement,
        "Epic Boon of Fate": "OBSOLETE",
        "Epic Boon of Spell Recall": "OBSOLETE",
        "Epic Boon of Truesight": "OBSOLETE",
    },
    "Holy Orders": {
        "Holy Order: Protector": HolyOrderProtector,
        "Holy Order: Scholar": HolyOrderScholar,
        "Holy Order: Thaumaturge": HolyOrderThaumaturge,
    },
    "Species": {
        # TODO The rest of the species
        # "Climber Ardling": ClimberArdling,
        # "Flyer Ardling": FlyerArdling,
        # "Racer Ardling": RacerArdling,
        # "Swimmer Ardling": SwimmerArdling,
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
        "Cloud Goliath": CloudGoliath,
        "Fire Goliath": FireGoliath,
        "Frost Goliath": FrostGoliath,
        "Hill Goliath": HillGoliath,
        "Stone Goliath": StoneGoliath,
        "Storm Goliath": StormGoliath,
    },
    "Spells": {
        "Aid": Aid,
        "Banishment": Banishment,
        "Guidance": Guidance,
        "Prayer of Healing": PrayerOfHealing,
        "Resistance": Resistance,
        "Spiritual Weapon": SpiritualWeapon,
    }
}
