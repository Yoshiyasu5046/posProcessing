#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import fileinput

# もっとシンプルに書けそう。
splitted_preLine = []
for line in fileinput.input():
	line = line.rstrip()
	splitted_line = line.split(' ')
	if splitted_preLine != []:
		preMemAndGId = splitted_preLine[0] + ':' + splitted_preLine[1] # gId = goodsId 
		memAndGId = splitted_line[0] + ':' + splitted_line[1]
		if preMemAndGId == memAndGId:
			total = int(splitted_preLine[2])
			total += int(splitted_line[2])
			# 現在の行の商品コード、会員番号、前の行との売上総数の合計をsplitted_preLine[0:2]に格納。
			splitted_preLine[0:2] = [splitted_line[0], splitted_line[1], str(total)]
		elif preMemAndGId != memAndGId:
			output = preMemAndGId + '\t' + splitted_preLine[2]
			print output
			# 現在の行の商品コード、会員番号、売上総数をsplitted_preLine[0:2]に格納。
			splitted_preLine[0:2] = [splitted_line[0], splitted_line[1], splitted_line[2]]
	else:
		splitted_preLine = splitted_line

# 最後の行の処理。最後の行はpreLineに格納されるだけのため、ループ後に出力する必要がある。
preMemAndGId = splitted_preLine[0] + ':' + splitted_preLine[1]
output = preMemAndGId + '\t' + splitted_preLine[2]
print output
