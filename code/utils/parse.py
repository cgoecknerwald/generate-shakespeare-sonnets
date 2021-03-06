# Parsing shakespeare.txt into quatrains and couplets
# "parsed_data.txt" will contain a list of quatrains, followed by a list of couplets, followed by a dictionary
# words will be encoded as unqiue numbers using the dictionary

from collections import defaultdict
from utils.vocal import count_syllables

# Helper function to separate the file into individual sonnets
def get_poems(reverse=False):
    with open('shakespeare.txt') as file:
        poems = []
        curr_poem = ''
        for line in file:
            if reverse:
                line = line.rstrip() # strip the newline
                line = line[::-1] + "\n" # dealing with newlines
            if len(line.strip().split()) > 1:
                curr_poem += line
            elif curr_poem:
                poems.append(curr_poem)
                curr_poem = ''
        if curr_poem:
            poems.append(curr_poem)
    return poems

def id_map(data):
    d = {}
    curr_ind = 0
    data_map = []
    for x in data:
        x_map = []
        for el in x:
            if el not in d:
                d[el] = curr_ind
                d[curr_ind] = el
                curr_ind += 1
            x_map.append(d[el])
        data_map.append(x_map)
    return data_map, d

def syl_map(data):
    d = defaultdict(set)
    data_map = []
    for x in data:
        x_map = []
        for el in x:
            ind = count_syllables(el)
            d[ind].add(el)
            x_map.append(ind)
        data_map.append(x_map)
    return data_map, d

# Main function, which separates quatrains and couplets
# Set reverse to true to receive data with each line backwards
def get_shakespeare(reverse=False, mapping='id'):
    poems = get_poems(reverse=reverse)
    lines = []
    for poem in poems:
        translator = str.maketrans('', '', ',:;.?!()')
        poem = poem.translate(translator)
        poem = poem.lower()
        poem = poem.strip().split('\n')

        # Discount Sonnets 99 and 126
        if len(poem) != 14:
            continue

        for line in poem:
            lines.append(line.split())

    if mapping == 'id':
        map_f = id_map
    elif mapping == 'syllables':
        map_f = syl_map
    else:
        raise Exception('Invalid mapping: {}'.format(mapping))
    lines, word_dict = map_f(lines)
    return lines, word_dict
