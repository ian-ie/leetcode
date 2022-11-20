#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for i in range(1, query_row + 1):
            nextRow = [0] * (i + 1)
            for j, val in enumerate(row):
                if val > 1:
                    nextRow[j] += (val - 1) / 2
                    nextRow[j + 1] += (val - 1) / 2
            row = nextRow
        return min(1, row[query_glass])


# @lc code=end
