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
			splitted_preLine[0] = splitted_line[0] # 現在の行の商品コードを前の行の商品コードしてsplitted_preLine[0]に格納。
			splitted_preLine[1] = splitted_line[1] # 現在の行の会員番号を前の行の会員番号してsplitted_preLine[1]に格納。
			splitted_preLine[2] = str(total) # 同じ商品コード：会員番号の組み合わせを持つ行の売上総数の合計をsplitted_preLine[2]に格納
		elif preMemAndGId != memAndGId:
			output = preMemAndGId + '\t' + splitted_preLine[2]
			print output
			splitted_preLine[0] = splitted_line[0] # 現在の行の商品コードを前の行の商品コードとしてsplitted_preLineに格納。
			splitted_preLine[1] = splitted_line[1] # 現在の行の会員番号を前の行の会員番号としてsplitted_preLine[1]に格納。
			splitted_preLine[2] = splitted_line[2] # 現在の行の売上総数を前の行の売上総数としてsplitted_preLine[1]に格納。
	else:
		splitted_preLine = splitted_line

# 最後の行の処理。最後の行はpreLineに格納されるだけのため、ループ後に出力する必要がある。
preMemAndGId = splitted_preLine[0] + ':' + splitted_preLine[1]
output = preMemAndGId + '\t' + splitted_preLine[2]
print output
