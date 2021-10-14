# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:03:58 2021

@author: pc03
"""
#
def process(w):
	output = " "
	for ch in w:
		if(ch.isalpha()): # 알파벳만 남기고 나머지 제거
			output +=ch
	return output.lower() #소문자로 바꿔서 리턴 
words = set()

# 1. 파일을 불러오기

fname = input("입력 파일 이름 : ")
file = open(fname, "r") # ==>c랑 동일

# 파일의 모든 줄에 대해 반복한다.
for line in file: #\n이 나올때까지의 한 줄을 가져온다.
	lineWords = line.split() # split하고 빈칸을 다 없애고 리스트로 만들어 준다. 그래서 line Words는 리스트가 된다.
	for word in lineWords:
		words.add(process(word)) # 단어를 세트에 추가한다.
print("사용된 단어의 개수 = ", len(words)) 
print(words)

#%%

"""def process(w):
	output = " "
	for ch in w:
		if(ch.isalpha()): # 알파벳만 남기고 나머지 제거
			output +=ch
        # value++
        return (output.lower(),value) #소문자로 바꿔서 리턴 """
table = dict() #딕셔너리 자료형으로 받아오기.

# 1. 파일을 불러오기

fname = input("입력 파일 이름 : ")
file = open(fname, "r") # ==> c랑 동일

# 파일의 모든 줄에 대해 반복한다.
for line in file: #\n이 나올때까지의 한 줄을 가져온다.
    words = line.split() # split하고 빈칸을 다 없애고 리스트로 만들어 준다. 그래서 line Words는 리스트가 된다.
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] +=1
#%%

put_name = 's'
address=dict()

put_mode = 's'
search_mode = 's'

while 1:
    put_name = input("(입력모드) 이름을 입력하세요 : ")
    if put_name != "":
        put_phone_num = input("(입력모드) 전화번호를 입력하세요 : ")
        address[put_name] = put_phone_num
    else:
            put_name = input("(검색모드) 이름을 입력하세요 : ")
            if put_name != "":
                if put_name in address:
                    print("{0}의 전화번호는 {1}입니다. ".format(put_name, put_phone_num))
                else:
                    print("찾으시는 이름이 없습니다.")   
            else:
                break


    