#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210728.py
# @Desc    : 
# @Time    : 2021/7/28 18:33
# @Author  : songpeiyao
# @Version : 1.0
"""
岛屿数量

给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

"""
from typing import List


class Solution:

    @staticmethod
    def left_right_is_land(i, j, grid):
        # 判断左边是否是陆地
        if j - 1 >= 0:
            if grid[i][j-1] == '1':
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def up_down_is_land(i, j, grid):
        # 判断上边是否是陆地
        if i - 1 >= 0:
            if grid[i-1][j] == '1':
                return True
            else:
                return False
        else:
            return False

    def numIslands(self, grid: List[List[str]]) -> int:
        # 遍历二维数组，当位置为1时，岛屿数量 +1
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    n += 1
                    # 判断四周是否陆地，如果是，n -= 1
                    if self.left_right_is_land(i, j, grid) or self.up_down_is_land(i, j, grid):
                        n -= 1
        return n


