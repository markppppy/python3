#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210607.py
# @Desc    : 
# @Time    : 2021/6/7 10:30
# @Author  : songpeiyao
# @Version : 1.0
"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
https://leetcode-cn.com/leetbook/read/array-and-string/ciekh/
输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""
from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # 先记录下所有为0的元素位置(如果直接把为0的行列设为0,会覆盖掉本来为0的元素, 影响后面的判断);
    iset = set()
    jset = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                iset.add(i)
                jset.add(j)
    # 把i行 matrix 元素设为0, 把j列 matrix 元素设为0
    for i in iset:
        matrix[i] = [0 for _ in matrix[i]]
    for i in range(len(matrix)):
        for j in jset:
            matrix[i][j] = 0
    # 可以优化为记录有0元素的行和列，然后遍历 matrix 的行列, 遇到前面记录的行或列，元素都设为0


if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(matrix)
    print(matrix)
