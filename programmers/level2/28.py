#28 번  폰켓몬


def solution(nums):
    answer = 0
    lenth = len(nums)//2
    nums.sort()
    last = 0
    for x in nums:
        if (x != last and answer < lenth):
            answer +=1
            last = x


    return answer


n=[3,1,2,3]
print(solution(n))