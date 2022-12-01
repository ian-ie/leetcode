#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min, index = float("inf"), -1
        for i, (px, py) in enumerate(points):
            if x == px:
                if (dist := abs(y - py)) < min:
                    min = dist
                    index = i
            elif y == py:
                if (dist := abs(x - px)) < min:
                    min = dist
                    index = i
        return index


# @lc code=end
