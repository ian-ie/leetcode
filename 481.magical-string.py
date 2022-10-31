#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#

# @lc code=start
s = [1, 2, 2]
i = 2
while len(s) < 100000:
    s += [s[-1] ^ 3] * s[i]
    i += 1
preSum = list(accumulate((2 - c for c in s), initial=0))


class Solution:
    def magicalString(self, n: int) -> int:
        return preSum[n]
        # if n < 4:
        #     return 1
        # s = [""] * n
        # s[:3] = "122"
        # count = 1
        # i, j = 2, 3
        # while j < n:
        #     length = int(s[i])
        #     num = 3 - int(s[j - 1])
        #     while length and j < n:
        #         s[j] = str(num)
        #         j += 1
        #         length -= 1
        #         count += 1 if num == 1 else 0

        #     i += 1
        # return count


# @lc code=end
