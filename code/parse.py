# Parsing shakespeare.txt into quatrains and couplets
# "parsed_data.txt" will contain a list of quatrains, followed by a list of couplets, followed by a dictionary
# words will be encoded as unqiue numbers using the dictionary

def get_shakespeare():
	inputfile = open("shakespeare.txt")

	dictionary = {} # {word: num, num: word, word2: num2, num2: word2 ...}

	dict_index = 0

	quatrains = []
	sub_quat = []
	count = 0
	couplets = []
	sub_coup = []

	for line in inputfile.readlines()[1:]: # we skip the first line
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
		elif "  " in line and "   " not in line:
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
		elif "   " in line:
			print(sub_quat)
			quatrains.append(sub_quat)
			couplets.append(sub_coup)
			sub_quat = []
			sub_coup = []

	inputfile.close()

	return quatrains, couplets, dictionary




