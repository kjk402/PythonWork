# Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            #i 다음 인덱스부터 loop
            for j in range(i+1, len(nums)):
                # 첫번째 인덱스부터 뒤에있는 인덱스를 더하고 target이 맞는지 확인
                if target == (nums[i] + nums[j]):
                    # target이 맞다면 2개 인덱스 리턴
                    return [i, j]


