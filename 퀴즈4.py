# 코딩대회를 주최함
# 댓글이벤트 1명 치킨 3명 커피
# 조건1 댓글은 20명이 작성했고 아이디는1~20으로 가정
# 조건2 무작위인데 중복 불가
# # 조건3 random과 shuffle과 sample사용

from random import*
num = range(1, 21)
num = list(num) 
shuffle(num)
num1 = sample(num, 4)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(num1[0]))
print("커피 당첨자 : {0}".format(num1[1:]))
print("--축하합니다--")
