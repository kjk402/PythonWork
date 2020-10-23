# 병합 정렬 merge sort

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def splitdata(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = splitdata(data[:medium])
    right = splitdata(data[medium:])
    return merge(left, right)

print(splitdata([5, 10, 37, 43, 61, 71, 77, 78, 82, 84]))