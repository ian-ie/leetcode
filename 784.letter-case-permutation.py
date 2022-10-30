#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(s: List[str], pos: int) -> None:
            while pos < len(s) and s[pos].isdigit():
                pos += 1
            if pos == len(s):
                res.append("".join(s))
                return

            dfs(s, pos + 1)
            s[pos] = s[pos].swapcase()
            dfs(s, pos + 1)
            s[pos] = s[pos].swapcase()

        dfs(list(s), 0)
        return res

        # alphaNum = sum(c.isalpha() for c in s)
        # for bit in range(1 << alphaNum):
        #     tmp, pos = [], 0
        #     for c in s:
        #         if c.isalpha():
        #             tmp.append(c.upper() if bit >> pos & 1 else c.lower())
        #             pos += 1
        #         else:
        #             tmp.append(c)
        #     res.append("".join(tmp))
        # return res


# @lc code=end
