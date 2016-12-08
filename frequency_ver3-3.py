# bin/python
# -*- coding: utf-8 -*-

inputted_file1 = open('output2.txt', 'r')
inputted_file2 = open('output3.txt', 'r+')
outputted_file = open('output4.txt', 'w')


arrayOfOverlapped = [] 
for item in inputted_file2:
	arrayOfOverlapped.append(item[:22])

for line in inputted_file1:
	if line[:22] not in arrayOfOverlapped:
		outputted_file.write(line)
	else:
		inputted_file2.write(line)

# for item in inputted_file2:
# 	#　inputted_file1の中身がなぜ1週しかループしないのか？itemの数だけループするはず。
# 	for line in inputted_file1:
# 		print line
# 		if item[:22] == line[:22]:
# 			outputted_file.write(item)


inputted_file1.close()
inputted_file2.close()
outputted_file.close()