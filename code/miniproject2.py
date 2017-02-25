from utils.parse import get_shakespeare, get_poems
from utils.vocal import count_syllables, get_rhyme_pair
from baum_welch.HMM import unsupervised_HMM

import random

distribution = [5] * 2 + [6] * 15 + [7] * 41 + [8] * 70 + [9] * 63 + [10] * 25

def generate_poem(reverse=False):
    lines, word_map = get_shakespeare(mapping='id', reverse=reverse)
    print('Training')
    model = unsupervised_HMM(lines, 6, 10)

    print('Emitting')
    print()

    poem = []
    for p in range(7):
        pair = []
        for end in get_rhyme_pair():
            initial_obs = [word_map[end]]
            num_words = random.choice(distribution)
            words = list(map(word_map.get, model.generate_emission(num_words, initial_obs)))
            while sum(map(count_syllables, words)) != 10:
                words = list(map(word_map.get, model.generate_emission(num_words, initial_obs)))
            words.reverse()
            pair.append(words)
        poem.append(pair)
    return poem

def reform(lst):
    lst = ['I' if w == 'i' else w for w in lst]
    lst[0] = lst[0].capitalize()
    return lst

poem = generate_poem()
for p in poem:
    print(p)
# poem = list(map(reform, poem))
# for i, line in enumerate(poem):
#     print('{i:<2} {line}'.format(i=i + 1, line=' '.join(line)))
