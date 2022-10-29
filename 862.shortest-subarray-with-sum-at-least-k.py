#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# @lc code=start
# TODO
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        preSum = [0]
        for val in nums:
            preSum.append(val + preSum[-1])

        q = deque()
        res = len(nums) + 1
        for ind, curSum in enumerate(preSum):
            while q and curSum - preSum[q[0]] >= k:
                res = min(res, ind - q.popleft())
            while q and preSum[q[-1]] >= curSum:
                q.pop()

            q.append(ind)
        return res if res <= len(nums) else -1


#         preSum = [0]
#         n = len(nums)
#         for val in nums:
#             preSum.append(val + preSum[-1])

#         res = -1
#         for l in range(n):
#             for r in range(l, n):
#                 if preSum[r + 1] - preSum[l] >= k:
#                     res = min(r + 1 - l, res) if res != -1 else r + 1 - l

#         return res
# @lc code=end
