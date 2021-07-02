# 35 소수 만들기

# 정수 배열이 주어지면 3개씩 더해서 만들 수 잇는 소수 개수 구하기

from itertools import combinations
import math
def solution(nums):
    cadidates = combinations(nums, 3)
    answer = 0
    for item in cadidates:
        sums = sum(item)
        is_prime = True
        for i in range(2, int(math.sqrt(sums)) + 1 ):
            if sums % i ==0:
                is_prime = False
                break
        if is_prime:
            answer +=1

    return answer

n = [1,2,3,4]
print(solution(n))


"""
def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
 
def solution(nums):
    answer = 0
    N = len(nums)
 
    for i in range(0, N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                total_num = nums[i] + nums[j] + nums[k]
                if isPrime(total_num):
                    answer += 1
 
    return answer
"""