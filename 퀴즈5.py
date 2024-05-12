# 50명의 매칭기회가 있을 때 총 탑승 승객 수 구하기
# 조건1 승객별 운행 소요시간은 5분 ~ 50분
# 조건2 소요시간 5분 ~ 15분 사이의 승객만 매칭

from random import*
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if time >= 5 and time <= 15:
        print("[성공] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[실패] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}".format(cnt))