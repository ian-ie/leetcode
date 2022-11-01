#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#

# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        aind = bind = i = j = 0
        while aind < len(word1) and bind < len(word2):
            if word1[aind][i] != word2[bind][j]:
                return False

            i += 1
            if i == len(word1[aind]):
                aind += 1
                i = 0

            j += 1
            if j == len(word2[bind]):
                bind += 1
                j = 0
        return aind == len(word1) and bind == len(word2)


# @lc code=end
