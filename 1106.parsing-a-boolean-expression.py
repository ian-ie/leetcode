#
# @lc app=leetcode.cn id=1106 lang=python3
#
# [1106] 解析布尔表达式
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ",":
                continue

            if c != ")":
                stack.append(c)
                continue

            t = f = 0
            while stack[-1] != "(":
                if stack.pop() == "t":
                    t += 1
                else:
                    f += 1
            stack.pop()
            opt = stack.pop()
            if opt == "!":
                stack.append("t" if f == 1 else "f")
            elif opt == "&":
                stack.append("t" if f == 0 else "f")
            elif opt == "|":
                stack.append("t" if t else "f")
        return stack[-1] == "t"


# @lc code=end
