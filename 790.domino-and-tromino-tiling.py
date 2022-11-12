#
# @lc app=leetcode.cn id=790 lang=python3
#
# [790] 多米诺和托米诺平铺
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        f = [[0] * 4 for _ in range(2)]
        f[1][0] = f[1][1] = 1
        for i in range(2, n + 1):
            x, y = i & 1, (i - 1) & 1
            f[x][0] = f[y][1]
            f[x][1] = sum(f[y][j] for j in range(4))
            f[x][2] = f[y][0] + f[y][3]
            f[x][3] = f[y][0] + f[y][2]
        return f[n & 1][1] % 1000000007


# @lc code=end
