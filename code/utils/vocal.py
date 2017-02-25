import os
import nltk
from nltk.corpus import cmudict
from random import choice, sample

d = cmudict.dict()
d['riper'] = ['R', 'AI0', 'PP', 'ER0']
d['buriest'] = ['B', 'UR0', 'IE0', 'E', 'ST0']
d['churl'] = ['CHURL0']
d['niggarding'] = ['0'] * 3
d['thriftless'] = ['0'] * 2
d['couldst'] = ['0'] * 2
d['viewest'] = ['0'] * 3
d['renewest'] = ['0'] * 3
d['unbless'] = ['0'] * 2
d['uneared'] = ['0'] * 2

def syllables(word):
    if word in d:
        # only care about one pronounciation.
        return len(list(y for y in d[word][0] if isdigit(y[-1])))
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count+=1
    if count == 0:
        count +=1
    return count

def isdigit(x):
    return x in '0123456789'

def count_syllables(word):
    w = word
    word = list(filter(bool, word.split("'")))[0]
    words = word.split("-")
    return sum(syllables(word) for word in words)


filename = os.path.join(os.path.dirname(__file__), 'rhyme_pairs.txt')
with open(filename) as file:
    rhyme = eval(file.read())

def get_rhyme_pair():
    return sample(choice(rhyme), 2)