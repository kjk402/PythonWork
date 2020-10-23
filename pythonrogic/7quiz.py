# # 표준체중 구하는 문제
#
# 남자: 키(m) x 키 x 22
# 여자: 키 x 키 x 21
#
# 조건1 : 표준체중은 별도의 함수 내에서 계산
#         *함수명: std_weight
#         *전달값: 키 height, 성별 gender
# 조건2 : 소수점 둘째자리까지표시

def std_weight(height, gender):
    if gender == "남":
        return height * height * 22

    else:
        return height * height *21


height = int(input())
gender = "여"
weight = round(std_weight(height /100, gender), 2)

print("키는 {0}cm {1}자의 표준체중은 {2}KG 입니다.".format(height, gender, weight))