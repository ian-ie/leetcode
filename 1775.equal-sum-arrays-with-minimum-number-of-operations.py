#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        def calc(map1, map2, diff):
            rmap = [0] * 7
            for i in range(1, 7):
                rmap[6 - i] += map1[i]
                rmap[i - 1] += map2[i]

            step = 0
            for i in range(5, 0, -1):
                if diff <= 0:
                    break
                t = min((diff + i - 1) // i, rmap[i])
                step += t
                diff -= t * i
            return step

        n, m = len(nums1), len(nums2)
        if 6 * n < m or 6 * m < n:
            return -1
        cnt1 = [0] * 7
        cnt2 = [0] * 7
        diff = 0
        for val in nums1:
            diff += val
            cnt1[val] += 1
        for val in nums2:
            diff -= val
            cnt2[val] += 1
        if diff == 0:
            return 0
        if diff > 0:
            return calc(cnt2, cnt1, diff)
        return calc(cnt1, cnt2, -diff)


# @lc code=end
