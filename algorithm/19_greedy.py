# 탐욕 알고리즘 Greedy algorithm

# 경우의 수가 있을 때 최적의 경우 선택하는 알고리즘

# 동전문제

coin_list = [1, 100, 50, 500]

def min_count(value, coin_list):
    total_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for i in coin_list:
        coin_num = value // i
        total_count += coin_num
        value -= coin_num * i
        details.append([i, coin_num])
    return total_count, details


print(min_count(4730, coin_list))


# 배낭문제
data_list = [(10,10), (15,12), (20,10), (25,8), (30,5)]


def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details