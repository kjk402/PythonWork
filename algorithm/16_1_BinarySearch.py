# 이진탐색 Binary Search

# 계속 중간값과 검색값 비교해서 탐색 범위를 줄이는 탐색

def binary(data, search):
    print(data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]: # 검색값이 중간값보다 커서 뒤에서 확인
            return binary(data[medium + 1:], search)
        elif search < data[medium]: # 검색값이 중간값보다 작으면 앞에서 확인
            return binary(data[:medium], search)



import random
data_list = random.sample(range(1,100), 10)
print(data_list)
data_list.sort()
print(binary(data_list, 51))
data_list.sort(reverse=True)
print(data_list)