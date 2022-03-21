#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210604.py
# @Desc    : 
# @Time    : 2021/6/4 19:33
# @Author  : songpeiyao
# @Version : 1.0
from typing import List

"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？

https://leetcode-cn.com/leetbook/read/array-and-string/clpgd/
"""


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # 水平翻转
    for i in range(n // 2):  # 前n//2行和后n//2行交换
        for j in range(n):  # i和j组成每次交换的元素
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]  # 列不变，只换行号
    # 主对角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]
              ]
    rotate(matrix)
    print(matrix)


