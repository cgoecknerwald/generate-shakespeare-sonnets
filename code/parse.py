# Parsing shakespeare.txt into quatrains and couplets
# "parsed_data.txt" will contain a list of quatrains, followed by a list of couplets, followed by a dictionary
# words will be encoded as unqiue numbers using the dictionary

import string

def get_poems():
    with open('shakespeare.txt') as file:
        poems = []
        curr_poem = ''
        for line in file:
            if len(line.strip().split()) > 1:
                curr_poem += line
            elif curr_poem:
                poems.append(curr_poem)
                curr_poem = ''
    return poems

def get_shakespeare():
    poems = get_poems()
    word_map = {}

    quatrains = []
    couplets = []

    for poem in poems:
        translator = str.maketrans('', '', ',:;.')
        poem = poem.translate(translator)
        poem = poem.lower()
        poem = poem.strip().split('\n')
        if len(poem) != 14:
            continue

        for i in range(0, 12, 4):
            q = []
            for line in poem[i : i + 4]:
                q.extend(line.split())
            quatrains.append(q)

        c = []
        c.extend(poem[12].split())
        c.extend(poem[13].split())

        quatrains.append(q)
        couplets.append(c)

    dq = {}
    curr_ind = 0
    quatrains_map = []
    couplets_map = []
    for q in quatrains:
        q_map = []
        for word in q:
            if word not in dq:
                dq[word] = curr_ind
                dq[curr_ind] = word
                curr_ind += 1
            q_map.append(dq[word])
        quatrains_map.append(q_map)

    dc = {}
    curr_ind = 0
    for c in couplets:
        c_map = []
        for word in c:
            if word not in dc:
                dc[word] = curr_ind
                dc[curr_ind] = word
                curr_ind += 1
            c_map.append(dc[word])
        couplets_map.append(c_map)
    return quatrains_map, couplets_map, dq, dc

