"""
Code to parse srd spells into json for use in later code generation
"""
import json
import string

txt = open('sources/parsed/srd_spells.txt', encoding='utf-8').read()
txt = txt.replace('\t', ' ').replace('’', "'")
STARTING_PAGE = 115
# txt = txt.split('\n')
# for x in txt[0:150]:
#    print(x)


LINES = txt.split('\n')
LINE_NUM = 0

SCHOOLS = ['Abjuration', 'Transmutation', 'Conjuration', 'Divination',
           'Enchantment', 'Illusion', 'Evocation', 'Necromancy']
LEVELS = ['1st-level',
          '2nd-level', '3rd-level', 'th-level']


def find_next_spell(lines) -> int:
    """
    Returns index in string of start of next spell in text
    """

    splits = [x + ' ' + y.lower() for x in LEVELS for y in SCHOOLS]
    splits += [x + ' cantrip' for x in SCHOOLS]

    for i, line in enumerate(lines):
        if any(kw in line for kw in splits) and lines[i-1][0].isupper():
            return i + 1
    return -1


def get_level_school(level_type: str) -> tuple[int, str]:
    """
    returns level and school from text
    """
    level = -1
    school = ''
    for digit in string.digits:
        if level_type.startswith(digit):
            level = int(digit)
            break
    if 'Cantrip' in level_type or 'cantrip' in level_type:
        level = 0

    for school in SCHOOLS:
        if school in level_type or school.lower() in level_type:
            school = school.title()
            break

    if level == -1 or school == '':
        print(level_type)
        raise Exception('get level fail')
    return level, school


def split_into_spell_text(lines: list[str]) -> list[str]:
    """
    splits arbitrary nonsense text into spell text
    """
    res = []
    cur = lines
    while (True):
        next_spell_index = find_next_spell(cur[2:])
        if next_spell_index <= 0:
            res.append('\n'.join(cur))
            break

        to_append = '\n'.join(cur[:next_spell_index])
        res.append(to_append)
        cur = cur[next_spell_index:]
    return res


def handle_pages(raw_spell_texts):
    """
    Takes text with page footers, then returns page range object with text
    """
    res = []
    current_page = 115
    for raw_spell_text in raw_spell_texts:
        split_text = raw_spell_text.split('\n')
        page_nums = [int(x[-3:]) for x in raw_spell_text.split(
            '\n') if 'System Reference' in x]
        clean_text = '\n'.join(
            x for x in split_text if 'System Reference' not in x)
        if len(page_nums) > 0:
            # crosses page
            pages = (current_page, page_nums[0]+1)
            current_page += 1
        else:  # same page
            pages = (current_page, current_page)

        res.append((pages, clean_text))
    return res


def get_casting_time(text: str) -> str:
    """
    method to sanity check casting time line
    """
    if 'Casting Time:' not in text:
        print(text)
        raise Exception('Casting time not in text')
    return text.replace('Casting Time:', '').strip()


def get_range(text: str) -> str:
    """
    method to sanity check the range line
    """
    if 'Range:' not in text:
        print('=====')
        print(text)
        print('=====')
        raise Exception('Range not in text')
    return text.replace('Range:', '').strip()


def get_components(text: str) -> tuple[bool, bool, str]:
    """
    sanity check and parse line into tuple of results
    """
    if 'Component' not in text:
        print(text)
        raise Exception('Component not in text')

    vsm, *component_list = text.split('(')
    verbal_components = 'V' in vsm
    somatic_components = 'S' in vsm

    return (verbal_components, somatic_components, ''.join(component_list).replace(')', ''))


def get_duration(text: str) -> str:
    """
    Sanity check for duration line
    """
    if 'Duration' not in text:
        print(text)
        raise Exception('Duration not in text')
    return text.replace('Duration:', '').strip()


def get_desc_higher_levels(lines: list[str]) -> tuple[str, str]:
    """
    Sanity check and parse description and at_higher_levels
    """
    text = '\n'.join(lines).replace('\n ', '\n').replace(
        "\n'", "'").replace(' \n', '\n')
    description, *higher_levels = text.split('At Higher Levels.')
    return (description.strip(), ''.join(higher_levels).strip())


def merge_markers(text: str, start: str, end: str) -> str:
    """
    Method to detect newlines between Range, Duration, Casting Time, etc.
    removes them
    """
    lines = text.split('\n')
    start_index = -1
    end_index = -1
    for i, line in enumerate(lines):
        if start in line and start_index == -1:
            start_index = i

        if end in line and end_index == -1:
            end_index = i

    if start_index > -1 and end_index > -1 and end_index > start_index:
        lines[start_index:end_index] = [
            ''.join(lines[start_index:end_index])]
        return '\n'.join(x for x in lines if x != '')
    else:
        print('-----')
        print(lines)
        print((start, end))
        print(start_index, end_index)
        raise Exception('start and end not in text')


def nudge_newlines(text: str) -> str:
    """
    Fix some of the newline nonsense in the original text
    """
    #print(' in nudge newlines ')
    splits = ['Casting Time', 'Range', 'Component', 'Duration']
    my_text = text
    for x in splits:
        if x in my_text:
            my_text = my_text.replace(x, '\n' + x)
    my_text = merge_markers(my_text, 'Casting Time', 'Range')
    my_text = merge_markers(my_text, 'Range', 'Component')
    my_text = merge_markers(my_text, 'Component', 'Duration')
    return my_text


def parse_spell(text: str, pages: tuple[int, int]):
    """
    Turn the text into a dict using helper methods
    """
    text = text.split('\n')
    name = text[0]
    level, school = get_level_school(text[1])
    casting_time = get_casting_time(text[2])
    spell_range = get_range(text[3])
    verbal_components, somatic_components, material_components_list = get_components(
        text[4])
    duration = get_duration(text[5])
    description, at_higher_levels = get_desc_higher_levels(text[6:])

    ret = {
        'name': name,
        'level': level,
        'school': school,
        'casting_time': casting_time,
        'spell_range': spell_range,
        'verbal_components': verbal_components,
        'somatic_components': somatic_components,
        'material_components_list': material_components_list,
        'duration': duration,
        'concentration': 'oncentration' in duration,
        'description': description,
        'at_higher_levels': at_higher_levels,
        'pages': pages
    }
    return ret


def parse_clean_spell_entries(cleaned: list[tuple]):
    """
    take cleaned spell text and pages, return json object list
    """
    ret = []
    for pages, spell_text in cleaned:
        ret.append(parse_spell(nudge_newlines(spell_text), pages))
    return ret


def parse_srd_spells():
    """
    parse the spells using helper functions
    """
    raw_spell_texts = split_into_spell_text(LINES)
    spell_text_with_range = handle_pages(raw_spell_texts)
    parsed = parse_clean_spell_entries(spell_text_with_range)
    open('sources/parsed/srd.json', 'w+',
         encoding='utf-8').write(json.dumps(parsed, indent=4))


parse_srd_spells()
