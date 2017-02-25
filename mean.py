# This file was used to determine the mean number of words per 10-syllable line
import numpy as np

file = open("shakespeare.txt")

lst = []

for line in file.readlines():
	line = line.strip().split()
	if len(line) > 1:
		lst.append(len(line))

for i in range(0,11):
	print(i, ":", lst.count(i))


lst = np.array(lst)
print (lst.mean(), lst.std())