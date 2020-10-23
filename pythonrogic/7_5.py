# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name,age), end="")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이: {1}\t".format(name,age), end="")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "python", "java", "c", "c++", "c#")
profile("김태호", 32, "kotlin", "python")