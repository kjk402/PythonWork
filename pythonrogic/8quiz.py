# # 보고서 기본 양식 만들기
# 1주차부터 50주까지 보고서 만들기
#
# 양식은 아래와 같다
# -- { }주차 주간보고--
# 부서:
# 이름:
# 업무 요약:

for i in range(1,11):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("--{0}주차 주간보고--".format(i))
        report_file.write("\n부서 :" + "\n이름 : " + "\n업무 요약 : ")