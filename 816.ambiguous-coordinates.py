#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def get_res(s: str) -> List[str]:
            res = []
            if len(s) == 1 or s[0] != "0":
                res.append(s)
            for ind in range(1, len(s)):
                # 00.01这种情况， 小数也不能尾数为0
                if s[0] == "0" and ind != 1 or s[-1] == "0":
                    continue

                res.append(s[:ind] + "." + s[ind:])
            return res

        ts = s[1:-1]
        n = len(ts)
        res = []
        for ind in range(1, n):
            ls = get_res(ts[:ind])
            if len(ls) == 0:
                continue

            rs = get_res(ts[ind:])
            if len(rs) == 0:
                continue

            for x, y in product(ls, rs):
                res.append(f"({x}, {y})")

        return res


# @lc code=end
