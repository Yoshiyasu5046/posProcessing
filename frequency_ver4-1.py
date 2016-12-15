#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

inputted_file = open(sys.argv[1], 'r')
outputted_file = open(sys.argv[2], 'w')

for line in inputted_file:	
	# rubyでいうchompと同様なものがpythonにはないので、rstrip()で代用。
	line = line.rstrip()
	splitted_input = line.split(',')
	goodsId = splitted_input[7]
	member = splitted_input[11]
	sales = splitted_input[9]
	output = goodsId + ' ' + member + ' ' + sales + '\n'
	outputted_file.write(output)


inputted_file.close()
outputted_file.close()