#입출력

print("Python", "Java", "C++",sep="VS", end="승자는?")
print("python")

score = {"수학":0, "영어":50, "코딩":100}
for subject, score in score.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")


for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))

answer = input("아무거나 입력하세요 :")
print("입력하신 값은 "+answer+"입니다.")