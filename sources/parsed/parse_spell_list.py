"""
    parse that source bb
"""

schools = ['Abjuration', 'Alteration', 'Conjuration', 'Divination',
           'Enchantment', 'Illusion', 'Invocation', 'Necromancy']


def get_school_name(school_raw: str):


def parse_single_spell(line):
    level, *name, school, ritual = line.split(' ')
    level = int(level)
    name = ' '.join(name)
    school = get_school_name(school)
    isRitual = (ritual == 'Yes')
    print(level)
    print(name)
    print(school)
    print(isRitual)


def count_schools_of_magic(lines):
    count = 0
    for line in lines:
        if 'SPELLS' in line:
            print(line)
            count += 1
    return count


def clean_source(raw_txt: str) -> list[str]:
    txt = txt.replace('\n', ' ')
    for x in '0123456789':
        txt = txt.replace(' ' + x + ' ', '\n' + x + ' ')
    txt = txt.replace('No ', 'No\n')
    txt = txt.replace('Lvl Spell School Ritual', '')
    txt = [x for x in txt.split('\n') if x != '']
    txt = '\n'.join(txt)
    txt = [x.strip()
           for x in txt.split('\n') if not 'Wizards of the Coast' in x]
    txt = [x for x in txt if 'Â©202' not in x]
    txt = '\n'.join(txt)
    txt = txt.replace('â€™', "'")
    txt = txt.split('\n')
    return txt


txt = open('sources\parsed\odnd2_spell_list.txt').read()
txt = clean_source(txt)


print(txt.split('\n')[3])


print(count_schools_of_magic(txt.split('\n')))
print(parse_single_spell(txt.split('\n')[3]))
