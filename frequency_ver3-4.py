# bin/python
# -*- coding: utf-8 -*-

inputted_file = open('output3.txt', 'r')
outputted_file = open('output5.txt', 'w')

# 膨大なデータを扱う際、このような配列を利用した処理は使用できるのか疑問。
arrayOfOverlapped = []
for line in inputted_file:
	if line[:22] not in arrayOfOverlapped:
		arrayOfOverlapped.append(line[:22])

for line in inputted_file:
	for item in arrayOfOverlapped:
		if line[:22] == item:
			


inputted_file.close()
outputted_file.close()
