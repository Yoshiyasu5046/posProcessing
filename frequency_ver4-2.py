# bin/python
# -*- coding: utf-8 -*-


inputted_file = open('output1.txt', 'r')
outputted_file = open('output2.txt', 'w')

preLine = ""
for line in inputted_file:
	if line[:22] == preLine[:22]:
		total = int(preLine[23])
		total += int(line[23])
		preLine = line[:23] + str(total) + '\n'
	elif line[:22] != preLine[:22]:
		if preLine != "":
			outputted_file.write(preLine)
		preLine = line

inputted_file.close()
outputted_file.close()
