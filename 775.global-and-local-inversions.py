#
# @lc app=leetcode.cn id=775 lang=python3
#
# [775] 全局倒置与局部倒置
#

# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        min_suf = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            if nums[i - 1] > min_suf:
                return False
            min_suf = min(min_suf, nums[i])

        return True


# @lc code=end
