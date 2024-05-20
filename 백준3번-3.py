# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성
a = int(input("숫자를 입력하시오. : "))
b = 0
for i in range(1, a+1):
    b += i
print("합 : {0}".format(b))