#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
from typing import DefaultDict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        kv = DefaultDict(int)
        for i, c in enumerate(order):
            kv[c] = i + 1

        return "".join(sorted(s, key=lambda c: kv[c]))


# @lc code=end
