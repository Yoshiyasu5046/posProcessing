# bin/python
# -*- coding: utf-8 -*-

inputted_file = open('sample_input.txt', 'r')
outputted_file = open('output1.txt', 'w')
for line in inputted_file:	
	splitted_input = line.split(',')
	if len(splitted_input[11]) > 8:
		splitted_input[11] = splitted_input[11][:8]
	member = splitted_input[11]
	goodsCode = splitted_input[7]
	salesOfGoods = splitted_input[9]
	output = member + ':' + goodsCode + '\t' + salesOfGoods + '\n'
	outputted_file.write(output)



