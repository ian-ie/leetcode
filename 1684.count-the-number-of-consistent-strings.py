#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask, res = 0, 0
        for c in allowed:
            mask |= (1 << ord(c) - ord("a"))

        for word in words:
            isTar = True
            for c in word:
                if not(mask >> (ord(c)-ord("a")) & 1):
                    isTar = False
                    break
            res += 1 if isTar else 0
        return res
# @lc code=end
