from utils.parse import get_shakespeare, get_poems
from utils.vocal import count_syllables, get_rhyme_pair
from baum_welch.HMM import unsupervised_HMM

import random

distribution = [5] * 2 + [6] * 15 + [7] * 41 + [8] * 70 + [9] * 63 + [10] * 25

def generate_poems(reverse=False, n_poems=1):
    lines, word_map = get_shakespeare(mapping='id', reverse=reverse)
    print('Training')
    model = unsupervised_HMM(lines, 6, 100)
    print('Writing')
    with open('../visualization/A_start.txt', 'w') as f:
            f.write(' '.join(map(str, model.A_start)))
            f.write('\n')
    with open('../visualization/A.txt', 'w') as f:
        for a in model.A:
            f.write(' '.join(map(str, a)))
            f.write('\n')
    with open('../visualization/O.txt', 'w') as f:
        for a in model.O:
            f.write(' '.join(map(str, a)))
            f.write('\n')
    with open('../visualization/word_map.txt', 'w') as f:
        for k, v in word_map.items():
            f.write('{} {}\n'.format(k, v))
            f.write('\n')
    quit()

    print('Emitting')
    print()

    for _ in range(n_poems):
        lines = []
        for p in range(7):
            for end in get_rhyme_pair():
                initial_obs = [word_map[end]]
                num_words = random.choice(distribution) - 1
                words = list(map(word_map.get, model.generate_emission(num_words, initial_obs)))
                count = 0
                while sum(map(count_syllables, words)) != 10:
                    if count >= 1000:
                        num_words = random.choice(distribution) - 1
                        count = 0
                    words = list(map(word_map.get, model.generate_emission(num_words, initial_obs)))
                    count += 1
                words.reverse()
                lines.append(words)
        poem = [lines[i] for i in [0, 2, 1, 3, 4, 6, 5, 7, 8, 10, 9, 11, 12, 13]]
        yield poem

def reform(lst):
    lst = ['I' if w == 'i' else w for w in lst]
    lst[0] = lst[0].capitalize()
    return lst

for poem_i, poem in enumerate(generate_poems(n_poems=154)):
    poem = list(map(reform, poem))
    print('\n\n' + ' ' * 19 + str(poem_i + 1))
    for i, line in enumerate(poem):
        print('{i:<2} {line}'.format(i=i + 1, line=' '.join(line)))
    print()
