# 9번 전화번호 목록


def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book ) -1):
        if phone_book[i] in phone_book[ i +1]:
            return False
    return answer


print(solution(["119" ,"97674223", "1195524421"]))