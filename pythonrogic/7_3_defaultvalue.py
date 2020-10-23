# 기본값

def profile(name, age, main_lang):
    print("이름은 {0}\t나이 : {1} \n잘하는 언어는 {2}".format(name, age, main_lang))


profile("유재석", 24, "Java")
profile("tiago", 29, "football")


# 나이가 같다면 굳이 입력할 필요 없으므로 기본값 설정
def profile(name, age=17, main_lang="파이썬"):
    print("이름은 {0}\t나이 : {1} \n잘하는 언어는 {2}".format(name, age, main_lang))

profile("박명수")