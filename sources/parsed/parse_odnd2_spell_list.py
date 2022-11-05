"""
    parse that source bb
"""

import os
import string
import json


class SpellListInfo:
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
        return '(' + self._name + ' ' + str(self._level) + ' ' + self._school + ' ' + str(self._is_ritual) + ' ' + self._spell_list + ')'

    def __repr__(self):
        return self._name + ' ' + str(self._level)
        + ' ' + self._school

    def __getitem__(self, arg):
        if arg == 'name':
            return self._name
        elif arg == 'level':
            return self._level
        elif arg == 'school':
            return self._school
        elif arg == 'is_ritual':
            return self._is_ritual
        elif arg == 'spell_list':
            return self._spell_list
        else:
            raise Exception('no attribute for spelllistinfo')

    def toJSON(self):
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

for school in schools:
    school_abbrs[school] = school

# Validation
for school in school_abbrs:
    failed = False
    if school_abbrs[school] not in schools:
        print(school)
        failed = True

    if failed:
        os._exit(1)


def parse_single_spell(line: list[str], spell_list: str) -> SpellListInfo:
    level, *name, school, ritual = line.split(' ')
    if 'Contact' in line:
        print(line)
    if spell_list == '' or level == '' or school == '' or ritual == '' or name is []:
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
        isRitual = (ritual == 'Yes')
    except:
        # print(line)
        # print(name)
        # print(school)
        # print(ritual)
        if school == 'Antipathy/Sympathy':
            print('what a funky little edge case :)')
            return SpellListInfo('Antipathy/Sympathy', level, 'Enchantment', False, spell_list)

        else:
            os._exit(1)

    return SpellListInfo(name, level, school, isRitual, spell_list)


def clean_source(raw_txt: str) -> list[str]:
    txt = raw_txt.replace('\n', ' ')
    txt = txt.replace('â€™', "'").replace('’', "'").replace(" '", "'")
    for x in string.digits:
        txt = txt.replace(' ' + x + ' ', '\n' + x + ' ')
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
    current_type = ''
    spells = []
    for line in lines:
        if any(line.startswith(x) for x in string.digits):
            spells.append(parse_single_spell(line, current_type))
        else:
            current_type = line.replace('SPELLS', '').strip().title()
    return spells


def update_or_initialize_spell(ret, field: str, spell: SpellListInfo):
    spellProperty = spell[field]
    if spellProperty not in ret[field]:
        ret[field][spellProperty] = [spell.toJSON()]
    else:
        ret[field][spellProperty].append(spell.toJSON())
    return ret


def generate_dataset(spells: list[SpellListInfo]):
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


txt = open('sources/parsed/odnd2_spell_list.txt').read()
txt = clean_source(txt)
raw_spell_list = parse(txt)

data = generate_dataset(raw_spell_list)

open('sources/parsed/odnd2.json',
     'w+').write(json.dumps([x.toJSON() for x in raw_spell_list], indent=4))

for x in data:
    for y in data[x]:
        if y == 'Acid Arrow':
            for z in data[x][y]:
                print(x, y, z)


print([x for x in raw_spell_list if 'Acid' in x['name']])
