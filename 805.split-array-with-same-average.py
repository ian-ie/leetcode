#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#

# @lc code=start
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # 可推出 sum(A)/k = sum(nums)/n
        n = len(nums)
        if n == 1:
            return False
        s = sum(nums)
        for i in range(n):
            # 避免原avg为浮点
            # 把avg变成0
            nums[i] = nums[i] * n - s

        m = n // 2
        left = set()
        for i in range(1, 1 << m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)
        # avg(nums) == 0, 若部分left = -rsum，则剩余left必为0，已经return了
        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True
        return False


# @lc code=end
