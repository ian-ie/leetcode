# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0

        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return (
                dfs(a - 4, b)
                + dfs(a - 3, b - 1)
                + dfs(a - 2, b - 2)
                + dfs(a - 1, b - 3)
            ) / 4

        return dfs(n, n)

        # dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        # dp[0] = [0.5] + [1.0] * n
        # for i in range(1, n + 1):
        #     for j in range(1, n + 1):
        #         dp[i][j] = (
        #             dp[max(0, i - 4)][j]
        #             + dp[max(0, i - 3)][max(0, j - 1)]
        #             + dp[max(0, i - 2)][max(0, j - 2)]
        #             + dp[max(0, i - 1)][max(0, j - 3)]
        #         )/4
        # print(dp)
        # return dp[n][n]


# @lc code=end
