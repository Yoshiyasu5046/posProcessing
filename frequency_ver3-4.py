# bin/python
# -*- coding: utf-8 -*-

inputted_file1 = open('output3.txt', 'r')
outputted_file = open('output5.txt', 'w')

# 膨大なデータを扱う際、このような配列を利用した処理は使用できるのか疑問。
arrayOfOverlapped = []
for line in inputted_file1:
	if line[:22] not in arrayOfOverlapped:
		arrayOfOverlapped.append(line[:22])

inputted_file1.close()


for item in arrayOfOverlapped:
	total = 0
	inputted_file1 = open('output3.txt', 'r')
	for line in inputted_file1:
		if line[:22] == item:
			total += int(line[23:])
			output = line[:23] 
	output += str(total) + '\n'
	outputted_file.write(output)
	inputted_file1.close()

inputted_file2 = open('output4.txt', 'r')
for line in inputted_file2:
	outputted_file.write(line)


inputted_file1.close()
inputted_file2.close()
outputted_file.close()
