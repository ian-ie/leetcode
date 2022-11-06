#
# @lc app=leetcode.cn id=1678 lang=python3
#
# [1678] 设计 Goal 解析器
#

# @lc code=start
class Solution:
    def interpret(self, command: str) -> str:
        res = [""]
        for i, c in enumerate(command):
            if c == "G":
                res.append("G")
            elif c == "(":
                res.append("o" if command[i + 1] == ")" else "al")

        return "".join(res)


# @lc code=end
