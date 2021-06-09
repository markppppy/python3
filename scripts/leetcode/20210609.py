#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210609.py
# @Desc    : 
# @Time    : 2021/6/8 19:36
# @Author  : songpeiyao
# @Version : 1.0
from typing import List
"""
最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"
"""


def findMaxStr(strs: List) -> str:
    n = len(strs[0])-1  # 每次循环从元素的索引n开始对比
    for l in range(len(strs)):
        # n 和 s的长度 两个数字取小的
        if n > len(strs[l]) - 1:
            n = len(strs[l]) - 1
        if l == 0:
            continue
        r = n
        while r >= 0:  # r是当前元素的索引
            if strs[l][r] != strs[l-1][r]:  # 每次对比当前元素索引n和前一个元素的索引n的值，如果不相等n-1
                n = r - 1  # n 和 r对应
            r -= 1
    return strs[0][:n+1]


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(findMaxStr(strs))
