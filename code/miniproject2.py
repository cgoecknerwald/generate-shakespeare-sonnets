from utils.parse import get_shakespeare, get_poems
from utils.vocal import count_syllables
from baum_welch.HMM import unsupervised_HMM

import random

distribution = [5] * 2 + [6] * 15 + [7] * 41 + [8] * 70 + [9] * 63 + [10] * 25

def generate_poem():
    q, c, dq, dc = get_shakespeare(mapping='id')
    print('Training')
    c_model = unsupervised_HMM(c, 3, 10)
    q_model = unsupervised_HMM(q, 6, 10)

    print('Emitting')
    print()

    poem = []
    for i in range(0,12):
        num_words = random.choice(distribution)
        words = list(map(dq.get, q_model.generate_emission(num_words)))
        while sum(map(count_syllables, words)) != 10:
            words = list(map(dq.get, q_model.generate_emission(num_words)))
        poem.append(words)
    for _ in range(0,2):
        num_words = random.choice(distribution)
        words = list(map(dc.get, c_model.generate_emission(num_words)))
        while sum(map(count_syllables, words)) != 10:
            words = list(map(dc.get, c_model.generate_emission(num_words)))
        poem.append(words)
    return poem

def reform(lst):
    lst = ['I' if w == 'i' else w for w in lst]
    lst[0] = lst[0].capitalize()
    return lst

poem = generate_poem()
poem = list(map(reform, poem))
for i, line in enumerate(poem):
    print('{i:<2} {line}'.format(i=i + 1, line=' '.join(line)))
