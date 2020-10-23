

absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        print("다음")
        continue
    elif student in no_book:
        print("오늘 수업끝 {0}번은 교무실로".format(student))
        break

    print("{0}번 책읽어".format(student))