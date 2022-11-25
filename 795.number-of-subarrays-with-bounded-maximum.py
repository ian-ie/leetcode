#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n, ans = len(nums), 0
        j, k = -1, -1
        for i in range(n):
            if nums[i] > right:
                k = i
            else:
                if nums[i] < left:
                    ans += j - k if j > k else 0
                else:
                    ans += i - k
                    j = i
        return ans


# @lc code=end
