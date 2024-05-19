# 표준 체중 구하는 프로그램
# 남자 : 키 * 키 * 22 
# 여자 : 키 * 키 * 21
# 조건 함수 stu_weight
#     전달값 키 height 성별 gender
# 표준체중 소수점 둘째자리까지 표시
def std_weight(height, gender):

    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}".format(height, gender, weight))