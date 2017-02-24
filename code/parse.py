# Parsing shakespeare.txt into quatrains and couplets
# "parsed_data.txt" will contain a list of quatrains, separated by Xs, followed by the couplets

def parse():
	inputfile = open("shakespeare.txt")

	quatrains = []
	sub_quat = []
	couplets = []
	sub_coup = []
	for line in inputfile.readlines()[1:]: # we skip the first line
		# no double spaces: quatrain line
		if "  " not in line:
			sub_quat += (line.strip().split())

		# 3 or more spaces: # line
		# reset the sub_quat and sub_coup arrays
		elif "   " in line:
			quatrains.append(sub_quat)
			couplets.append(sub_coup)
			sub_quat = []
			sub_coup = []

		# 2 spaces: couplet line
		elif "  " in line and "   " not in line:
			sub_coup += line.strip().split()



	# separate quatrain lines into groups of 4

	inputfile.close()

	return quatrains, couplets


print(parse())




