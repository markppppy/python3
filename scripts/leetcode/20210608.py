#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210608.py
# @Desc    : 
# @Time    : 2021/6/7 19:12
# @Author  : songpeiyao
# @Version : 1.0


"""
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
https://leetcode-cn.com/leetbook/read/array-and-string/cuxq3/

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]
"""
from typing import List


def findDiagonalOrderImitate(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    N, M = len(matrix), len(matrix[0])
    im = []
    target = []
    for d in range(M+N-1):
        im.clear()
        r, c = 0 if d < M else d - M + 1, d if d < M else M-1
        # 循环以r,c 为端点的对角线元素，放入 im
        while r < N and c > -1:  # !
            im.append(matrix[r][c])
            r += 1
            c -= 1

        if d % 2 == 0:
            target.extend(im[::-1])  # im倒序加入target
        else:
            target.extend(im)
    return target


def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:

    # Check for empty matrices
    if not matrix or not matrix[0]:
        return []

    # Variables to track the size of the matrix
    N, M = len(matrix), len(matrix[0])

    # The two arrays as explained in the algorithm
    result, intermediate = [], []

    # We have to go over all the elements in the first
    # row and the last column to cover all possible diagonals
    for d in range(N + M - 1):

        # Clear the intermediate array everytime we start
        # to process another diagonal
        intermediate.clear()

        # We need to figure out the "head" of this diagonal
        # The elements in the first row and the last column
        # are the respective heads.
        # r, c是对角线最外层第一个元素的下标
        r, c = 0 if d < M else d - M + 1, d if d < M else M - 1

        # Iterate until one of the indices goes out of scope
        # Take note of the index math to go down the diagonal
        while r < N and c > -1:
            intermediate.append(matrix[r][c])
            r += 1
            c -= 1

        # Reverse even numbered diagonals. The
        # article says we have to reverse odd
        # numbered articles but here, the numbering
        # is starting from 0 :P
        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)
    return result


"""
初始化数组 result，用于存储最后结果。

使用一个外层循环遍历所有的对角线。第一行和最后一列的元素都是对角线的起点。

使用一个内层 while 循环遍历对角线上的所有元素。可以计算指定对角线上的元素数量，也可以简单迭代直到索引超出范围。

因为不知道每条对角线上的元素数量，需要为每条对角线分配一个列表或动态数组。但是同样也可以通过计算得到当前对角线上的元素数量。

对于奇数编号的对角线，只需要将迭代结果翻转再加入结果数组即可。

"""

if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(findDiagonalOrderImitate(mat))

