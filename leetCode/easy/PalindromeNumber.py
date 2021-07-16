# Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        length = len(number)
        is_even = False
        if x < 0:
            return False
        if length == 0:
            return False
        if length % 2 == 0:
            return False

        middle = length // 2

        last_index = length -1
        for i in range(middle, length):
            if not is_even:
                is_even = True
                continue
            opp = last_index - i
            if number[opp] != number[i]:
                return False
        return True