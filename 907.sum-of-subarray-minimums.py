#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(-1)
        ans, st = 0, [-1]
        for r, x in enumerate(arr):
            while len(st) > 1 and arr[st[-1]] >= x:
                i = st.pop()
                ans += arr[i] * (i - st[-1]) * (r - i)
            st.append(r)
        return ans % (10**9 + 7)


# @lc code=end
