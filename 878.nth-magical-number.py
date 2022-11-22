#
# @lc app=leetcode.cn id=878 lang=python3
#
# [878] 第 N 个神奇数字
#

# @lc code=start
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        l = min(a, b)
        r = n * l
        c = lcm(a, b)
        while l < r:
            mid = (l + r) // 2
            cnt = mid // a + mid // b - mid // c
            if cnt >= n:
                r = mid
            else:
                l = mid + 1
        return r % MOD


# @lc code=end
