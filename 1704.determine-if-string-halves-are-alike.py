#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = "AEIOUaeiou"
        n = len(s)
        a ,b = s[:n//2], s[n//2:]
        return sum(c in vowel for c in a) == sum(c in vowel for c in b)
# @lc code=end
