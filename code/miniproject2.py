from utils.parse import get_shakespeare, get_poems
from utils.vocal import count_syllables
from baum_welch.HMM import unsupervised_HMM

import random

distribution = [5] * 2 + [6] * 15 + [7] * 41 + [8] * 70 + [9] * 63 + [10] * 25

def train():
    q, c, dq, dc = get_shakespeare(mapping='id')
    print('Training')
    c_model = unsupervised_HMM(c, 6, 10)
    q_model = unsupervised_HMM(q, 6, 10)

    print('Emitting')
    sample = lambda x: random.sample(x, 1)[0]
    for i in range(0,12):
        num_words = random.choice(distribution)
        words = map(lambda x: sample(dq[x]), q_model.generate_emission(num_words))
        while sum(map(count_syllables, words)) != 10:
            words = map(lambda x: sample(dq[x]), q_model.generate_emission(num_words))
        print(' '.join(words))
    for _ in range(0,2):
        num_words = random.choice(distribution)
        words = map(lambda x: sample(dc[x]), c_model.generate_emission(num_words))
        while sum(map(count_syllables, words)) != 10:
            words = map(lambda x: sample(dc[x]), c_model.generate_emission(num_words))
        print(' '.join(words))

train()