# bin/python
# -*- coding: utf-8 -*-

# import re

inputted_file = open('output1.txt', 'r')
outputted_file1 = open('output3.txt', 'w')

# outputted_fileの中にあるlineの会員番号：商品コードがoutputted_fileにあるかどうかを
# 出来る限り短かいコードで処理するにはどうすればいいか？正規表現をどのように用いればこれができるか。
# そもそも正規表現を使用する必要性についても考えなければならない。どういう場合に正規表現クラスを
# 利用するべきかをわかった上で用いるべき。
# 開いたファイルを閉じるタイミング。そもそも閉じる必要はあるのか。そうだとするといつ閉じるべきか。
# 膨大なデータを扱う際、このような配列を利用した処理は使用できるのか疑問。
arrayOfOverlapped = []
for line in inputted_file:
	outputted_file2 = open('output2.txt', 'r+')
	for item in outputted_file2:
		if item[:22] == line[:22]:
			outputted_file1.write(line)
			arrayOfOverlapped.append(line[:22])
	if line[:22] not in arrayOfOverlapped:
		outputted_file2.write(line)
	
	# sample = re.search(line, outputted_file2, re.MULTILINE)
	# print sample
	# outputted_file1.write(line)
	
	# outputted_file2.write(line)


inputted_file.close()
outputted_file1.close()
outputted_file2.close()