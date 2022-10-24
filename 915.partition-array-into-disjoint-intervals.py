#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # n = len(nums)
        # rmin = [0] * n
        # rmin[-1] = nums[-1]
        # for ind in range(n - 2, 0, -1):
        #     rmin[ind] = min(nums[ind], rmin[ind + 1])

        # lmax = nums[0]
        # for ind in range(1, n):
        #     if lmax < rmin[ind]:
        #         return ind
        #     lmax = max(lmax, nums[ind])

        n = len(nums)
        lmax = cmax = nums[0]
        pos = 0
        for ind in range(1, n - 1):
            cmax = max(cmax, nums[ind])
            if nums[ind] < lmax:
                pos = ind
                lmax = cmax
        return pos + 1


# @lc code=end
