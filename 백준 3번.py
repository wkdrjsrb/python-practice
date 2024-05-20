# N을 입력받은 뒤 구구단 N단을 출력하는 프로그램
num = int(input("출력할 숫자를 입력하시오 : "))
for i in range(1, 10):
    print("{0} * {1} = {2}".format(num, i, num * i), end = ' ')