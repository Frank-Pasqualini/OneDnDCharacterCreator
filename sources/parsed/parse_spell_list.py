"""
    parse that source bb
"""

import os


class SpellListInfo:
    _name: str
    _level: int
    _school: str
    _is_ritual: bool
    _spell_type: str

    def __init__(self, name: str, level: int, school: str, is_ritual: bool, spell_type: str):
        self._name = name
        self._level = level
        self._school = school
        self._is_ritual = is_ritual
        self._spell_type = spell_type

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_school(self):
        return self._school

    def get_is_ritual(self):
        return self._is_ritual

    def get_spell_type(self):
        return self._spell_type

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name


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


def parse_single_spell(line: list[str], spell_type: str):
    level, *name, school, ritual = line.split(' ')
    if spell_type == '':
        raise Exception('spell_type cannot be empty')
    try:
        level = int(level)
        name = ' '.join(name)
        school = school_abbrs[school]
        isRitual = (ritual == 'Yes')
    except:
        print(line)
        print(name)
        print(school)
        print(ritual)
        if school == 'Antipathy/Sympathy':
            print('what a funky little edge case :)')
            return SpellListInfo('Antipathy/Sympathy', level, 'Enchantment', False, spell_type)

        else:
            os._exit(1)

    return SpellListInfo(name, level, school, isRitual, spell_type)
    return {
        'level': level,
        'name': name,
        'school': school,
        'is_ritual': isRitual,
        'spell_type': spell_type
    }


def count_schools_of_magic(lines):
    count = 0
    for line in lines:
        if 'SPELLS' in line:
            print(line)
            count += 1
    return count


def clean_source(raw_txt: str) -> list[str]:
    txt = raw_txt.replace('\n', ' ')
    txt = txt.replace('â€™', "'")
    for x in '0123456789':
        txt = txt.replace(' ' + x + ' ', '\n' + x + ' ')
    txt = txt.replace('No ', 'No\n')
    txt = txt.replace('Lvl Spell School Ritual', '')
    txt = txt.replace('/ ', '/')
    txt = [x for x in txt.split('\n') if x != '']
    txt = [x.strip() for x in txt if not 'Wizards of the Coast' in x]
    txt = [x for x in txt if 'Â©202' not in x]
    return txt


def parse(lines: list[str]) -> list:
    current_type = ''
    spells = []
    for line in lines:
        if any(line.startswith(x) for x in '0123456789'):
            spells.append(parse_single_spell(line, current_type))
        else:
            current_type = line.replace('SPELLS', '').strip().title()
    return spells


def generate_dataset(spells: list[SpellListInfo]):
    ret = {
        'name': {},
        'is_ritual': {},
        'school': {},
        'level': {},
        'spell_type': {}
    }

    for spell in spells:
        name = spell.get_name()
        is_ritual = spell.get_is_ritual()
        school = spell.get_school()
        level = spell.get_level()
        spell_type = spell.get_spell_type()

        if name not in ret['name']:
            ret['name'][name] = []

        if is_ritual not in ret['is_ritual']:
            ret['is_ritual'][is_ritual] = []

        if school not in ret['school']:
            ret['school'][school] = []

        if level not in ret['level']:
            ret['level'][level] = []

        if spell_type not in ret['spell_type']:
            ret['spell_type'][spell_type] = []

        ret['name'][name].append(spell)
        ret['is_ritual'][is_ritual].append(spell)
        ret['school'][school].append(spell)
        ret['level'][level].append(spell)
        ret['spell_type'][spell_type].append(spell)
    return ret


txt = open('sources\parsed\odnd2_spell_list.txt').read()
txt = clean_source(txt)
raw_spell_list = parse(txt)
data = generate_dataset(raw_spell_list)
for x in data:
    for y in data[x]:
        for z in data[x][y]:
            print(x, y, z)
