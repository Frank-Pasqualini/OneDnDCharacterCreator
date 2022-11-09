"""
Parse the odnd2 spell list into json
"""

import sys
import string
import json


class SpellListInfo:
    """
    Data portion of Spell class
    """
    _name: str
    _level: int
    _school: str
    _is_ritual: bool
    _spell_list: str

    def __init__(self, name: str, level: int, school: str, is_ritual: bool, spell_list: str):
        self._name = name
        self._level = level
        self._school = school
        self._is_ritual = is_ritual
        self._spell_list = spell_list

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_school(self):
        return self._school

    def get_is_ritual(self):
        return self._is_ritual

    def get_spell_list(self):
        return self._spell_list

    def __str__(self):
        return ('(' + self._name + ' ' + str(self._level) + ' ' + self._school + ' ' +
                str(self._is_ritual) + ' ' + self._spell_list + ')')

    def __repr__(self):
        return self._name + ' ' + str(self._level) + ' ' + self._school

    def __getitem__(self, arg):
        if arg == 'name':
            return self._name
        if arg == 'level':
            return self._level
        if arg == 'school':
            return self._school
        if arg == 'is_ritual':
            return self._is_ritual
        if arg == 'spell_list':
            return self._spell_list
        raise Exception('no attribute for spelllistinfo')

    def to_json(self):
        return {
            'name': self['name'],
            'level': self['level'],
            'school': self['school'],
            'is_ritual': self['is_ritual'],
            'spell_list': self['spell_list']
        }


schools = ['Abjuration', 'Transmutation', 'Conjuration', 'Divination',
           'Enchantment', 'Illusion', 'Evocation', 'Necromancy']

school_abbrs = {
    'Illusion*': 'Illusion',
    'Evocation': 'Evocation',
    'Transmut.': 'Transmutation',
    'Transmut.*': 'Transmutation',
    'Evocation*': 'Evocation',
    'Divination*': 'Divination',
    'Abjuration*': 'Abjuration',
    'Enchantment*': 'Enchantment',
    'Necromancy*': 'Necromancy'
}


def generate_school_abbrs():
    """
    generate school abbreviations
    """
    for school in schools:
        school_abbrs[school] = school

    # Validation
    for school, map_to in school_abbrs.items():
        if map_to not in schools:
            print(school)
            sys.exit(1)


def parse_single_spell(line: list[str], spell_list: str) -> SpellListInfo:
    """
    Parses spell into object
    """
    level, *name, school, ritual = line.split(' ')
    if 'Contact' in line:
        print(line)
    if spell_list == '' or level == '' or school == '' or ritual == '' or name == []:
        print(level)
        print(name)
        print(school)
        print(school)
        print(ritual)
        raise Exception('field cannot be empty')
    try:
        level = int(level)
        name = ' '.join(name)
        school = school_abbrs[school]
        is_ritual = (ritual == 'Yes')
    except Exception as ex:
        if school == 'Antipathy/Sympathy':
            return SpellListInfo('Antipathy/Sympathy', level, 'Enchantment', False, spell_list)
        print(ex)
        sys.exit(1)

    return SpellListInfo(name, level, school, is_ritual, spell_list)


def clean_source(raw_txt: str) -> list[str]:
    """
    lots of preprocess
    """
    txt = raw_txt.replace('\n', ' ')
    txt = txt.replace('â€™', "'").replace('’', "'").replace(" '", "'")
    for digit in string.digits:
        txt = txt.replace(' ' + digit + ' ', '\n' + digit + ' ')
    txt = txt.replace('No ', 'No\n')
    txt = txt.replace('Lvl Spell School Ritual', '')
    txt = txt.replace('/ ', '/')
    txt = txt.replace('Â©202', '\nÂ©202')
    txt = [x for x in txt.split('\n') if x != '']
    print('Contact Other' in ''.join(txt))
    print([x for x in txt if 'Wizards of the' in x])
    txt = [x.strip() for x in txt if not 'Wizards of the Coast' in x]
    print('Contact Other' in ''.join(txt))
    txt = [x for x in txt if 'Â©202' not in x]
    return txt


def parse(lines: list[str]) -> list[SpellListInfo]:
    """
    Outermost parsing loop. Tracks list type and calls helpers
    """
    current_type = ''
    spells = []
    for line in lines:
        if any(line.startswith(x) for x in string.digits):
            spells.append(parse_single_spell(line, current_type))
        else:
            current_type = line.replace('SPELLS', '').strip().title()
    return spells


def update_or_initialize_spell(ret, field: str, spell: SpellListInfo):
    """
    helper to deal with potentially empty dict
    """
    spell_property = spell[field]
    if spell_property not in ret[field]:
        ret[field][spell_property] = [spell.to_json()]
    else:
        ret[field][spell_property].append(spell.to_json())
    return ret


def generate_dataset(spells: list[SpellListInfo]):
    """
    generates useful ways of indexing spell list
    """
    ret = {
        'name': {},
        'is_ritual': {},
        'school': {},
        'level': {},
        'spell_list': {}
    }

    for spell in spells:
        for field in ['name', 'is_ritual', 'school', 'level', 'spell_list']:
            ret = update_or_initialize_spell(ret, field, spell)

    return ret


def generate_odnd2_spells():
    """
    Generate the odnd2 spell json
    """
    with open('sources/parsed/odnd2_spell_list.txt', 'r', encoding='utf-8') as fil:
        txt = fil.read()

    txt = clean_source(txt)
    raw_spell_list = parse(txt)

    data = generate_dataset(raw_spell_list)

    for spell_name in data['name']:
        spells = data['name'][spell_name]
        if len(spells) > 1:
            print(spells[0]['name'])
            merged = [x['spell_list'] for x in spells]
            spells[0]['spell_list'] = merged
            data['name'][spell_name] = spells[0]
        else:
            spell = spells[0]
            spell['spell_list'] = [spell['spell_list']]
            data['name'][spell_name] = spell

    with open('sources/parsed/odnd2.json', 'w+', encoding='utf-8') as fil:
        fil.write(json.dumps([data['name'][x]
                  for x in data['name']], indent=4))


generate_school_abbrs()
generate_odnd2_spells()
