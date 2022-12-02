#
# @lc app=leetcode.cn id=1769 lang=python3
#
# [1769] 移动所有球到每个盒子所需的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left, right, opt = int(boxes[0]), 0, 0
        for i in range(1, len(boxes)):
            if boxes[i] == "1":
                right += 1
                opt += i
        res = [opt]
        for i in range(1, len(boxes)):
            opt += left - right
            if boxes[i] == "1":
                left += 1
                right -= 1
            res.append(opt)

        return res


# @lc code=end
