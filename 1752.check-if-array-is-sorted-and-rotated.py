#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        t, n = 0, len(nums)
        for i in range(1, n):
            if t > 1:
                return False
            if nums[i - 1] > nums[i]:
                t += 1
        return t == 0 or (t == 1 and nums[0] >= nums[n - 1])


# @lc code=end
