#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        if n < m:
            return 0

        f = [0] * n
        for i in range(m - 1, n):
            equal = True
            for j in range(m):
                if sequence[i - m + j + 1] != word[j]:
                    equal = False
                    break
            if equal:
                f[i] = (0 if i == m - 1 else f[i - m]) + 1

        return max(f)


# @lc code=end
