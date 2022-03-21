#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210625.py
# @Desc    : 
# @Time    : 2021/6/25 9:54
# @Author  : songpeiyao
# @Version : 1.0

"""
杨辉三角

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1],
# [1,5,10,10,5,1]
]

杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

输入: 3
输出: [1,3,3,1]

你可以优化你的算法到 O(k) 空间复杂度吗？
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    # 从顶层循环，第一层设置初始值，后面层满足条件设置为条件值，不满足条件设置为1
    init_lst = [[1]]
    if numRows == 0:
        return []
    elif numRows == 1:
        return init_lst
    for n in range(1, numRows):
        # sub_init_lst = [1] * (n+1)
        sub_init_lst = []
        for sub in range(n+1):  # n=1时循环2次
            # numRows [n, sub]
            if sub - 1 >= 0 and sub <= len(init_lst[n - 1]) - 1:
                cur = init_lst[n-1][sub-1] + init_lst[n-1][sub]
                sub_init_lst.append(cur)
            else:
                cur = 1
                sub_init_lst.append(cur)
        init_lst.append(sub_init_lst)
    return init_lst


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [1] * (rowIndex + 1)
    for i in range(2, rowIndex + 1):
        for j in range(i - 1, 0, -1):
            res[j] += res[j - 1]
    return res


def getRow_(rowIndex: int) -> List[int]:
    # 抄的，滚动数组
    res = [1] * (rowIndex+1)
    for i in range(2, rowIndex+1):
        for j in range(i-1, 0, -1):
            res[j] += res[j-1]
    return res


if __name__ == '__main__':
    print(getRow(4))
    # print(generate(5))

