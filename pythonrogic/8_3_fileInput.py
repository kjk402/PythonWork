# 파일 입출력
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
# w 처음부터 쓰기 a 이어서 추가쓰기

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\ncoding :100")
score_file.close()





