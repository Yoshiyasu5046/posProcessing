#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import fileinput

for line in fileinput.input():	
	text = '\d+'
	if re.search(text, line):
		# rubyでいうchompと同様なものがpythonにはないので、rstrip()で代用。
		line = line.rstrip()
		splitted_input = line.split(',')
		goodsId = splitted_input[7]
		member = splitted_input[11]
		sales = splitted_input[9]
		output = goodsId + ' ' + member + ' ' + sales
		print output
