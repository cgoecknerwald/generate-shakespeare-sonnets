import nltk
from nltk.corpus import cmudict
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
    if not word:
        return 0
    if word in d:
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
    words_ = list(filter(bool, word.split("'")))
    if len(words_) == 0:
        return 0
    word = words_[0]
    words = word.split("-")
    for word in words:
        if not word:
            input(w)
    # only care about one pronounciation.
    return sum(syllables(word) for word in words)
