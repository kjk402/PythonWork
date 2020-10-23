# 퀵정렬 quick sort

def quicksort(data):
    if len(data)<= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    return quicksort(left) + [pivot] + quicksort(right)

num = list(map(int, input().split()))

print(quicksort(num))