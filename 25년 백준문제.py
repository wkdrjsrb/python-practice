# 백준 1037번: 약수

# 진짜 약수의 개수 입력
n = int(input())

# 진짜 약수들을 공백으로 구분해 입력받음
divisors = list(map(int, input().split()))

# 약수들을 정렬 (가장 작은 약수와 큰 약수를 찾기 위함)
divisors.sort()

# 가장 작은 약수 × 가장 큰 약수 = N
print(divisors[0] * divisors[-1])

