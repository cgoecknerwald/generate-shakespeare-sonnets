# Parsing shakespeare.txt into quatrains and couplets
# "parsed_data.txt" will contain a list of quatrains, followed by a list of couplets, followed by a dictionary
# words will be encoded as unqiue numbers using the dictionary

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
    curr_ind = 0

    quatrains = []
    couplets = []

    for poem in poems:
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

    d = {}
    quatrains_map = []
    couplets_map = []
    for q in quatrains:
        q_map = []
        for word in q:
            if word not in d:
                d[word] = curr_ind
                d[curr_ind] = word
                curr_ind += 1
            q_map.append(d[word])
        quatrains_map.append(q_map)

    for c in couplets:
        c_map = []
        for word in c:
            if word not in d:
                d[word] = curr_ind
                d[curr_ind] = word
                curr_ind += 1
            c_map.append(d[word])
        couplets_map.append(c_map)
    return quatrains_map, couplets_map, d

def _get_shakespeare():
    inputfile = open("shakespeare.txt")

    dictionary = {} # {word: num, num: word, word2: num2, num2: word2 ...}

    dict_index = 0

    quatrains = []
    sub_quat = []
    count = 0
    couplets = []
    sub_coup = []

    for line in inputfile.readlines():
        # no double spaces: quatrain line
        if "  " not in line:
            # convert words to numbers
            words = line.strip().split()
            nums = []
            for word in words:
                if word in dictionary:
                    nums.append(dictionary[word])
                else: # add a new, uniquely numbered entry for the word
                    dictionary[word] = dict_index
                    dictionary[dict_index] = word # dual mapping
                    nums.append(dict_index)
                    dict_index += 1 # increment the unique number

            # continue adding to our array
            sub_quat += list(nums)
            count += 1

            # if we have four lines in our array, append it to the larger array and restart
            if count == 4:
                quatrains.append(sub_quat)
                sub_quat = []
                count = 0

        # 2 spaces: couplet line
        elif "   " not in line:
            # convert words to numbers
            words = line.strip().split()
            nums = []
            for word in words:
                if word in dictionary:
                    nums.append(dictionary[word])
                else: # add a new, uniquely numbered entry for the word
                    dictionary[word] = dict_index
                    dictionary[dict_index] = word # dual mapping
                    nums.append(dict_index)
                    dict_index += 1 # increment the unique number

            # add the array of numbers
            sub_coup += nums

        # 3 or more spaces: # line
        # reset the sub_quat and sub_coup arrays
        elif sub_quat:
            quatrains.append(sub_quat)
            couplets.append(sub_coup)
            sub_quat = []
            sub_coup = []

    inputfile.close()

    return quatrains, couplets, dictionary




