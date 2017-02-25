file = open("shakespeare.txt")

# Helper function to separate the file into individual sonnets
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
        if curr_poem:
            poems.append(curr_poem)
    return poems

def get_rhyme_pairs():
    rhyming_pairs = []
    lst = []
    for i,poem in enumerate(get_poems()):
        if i == 99-1 or i == 126-1:
            continue # these are not real sonnets
        # expect abab cdcd efef gg
        lines = poem.split("\n")
        sublst = []
        for line in lines:
            if line:
                line = line.rstrip()
                last_word = line.split(" ")[-1]
                # remove any punctuation
                translator = str.maketrans('', '', ',:;\'.?!')
                last_word = last_word.translate(translator)
                sublst.append(last_word)
        lst.append(sublst)
        sublst = []
    for wordset in lst:
        for i in [0,1,4,5,8,9]:
            rhyming_pairs.append([wordset[i], wordset[i+2]])
        rhyming_pairs.append([wordset[12], wordset[13]])

    return rhyming_pairs

def combine_pairs():

print(get_rhyme_pairs())
