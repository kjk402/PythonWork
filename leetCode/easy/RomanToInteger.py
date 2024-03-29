# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        for i in range(len(s) - 1):
            num = dic[s[i]]
            nextNum = dic[s[i + 1]]
            if (num >= nextNum):
                result += num
            else:
                result -= num

        result += dic[s[len(s) - 1]]

        return (result)
