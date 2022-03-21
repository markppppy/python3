#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210601.py
# @Desc    : 
# @Time    : 2021/6/1 17:22
# @Author  : songpeiyao
# @Version : 1.0
from typing import List

"""
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
"""


def maxArea(height: List[int]) -> int:
    """
    思路：要求的最大值为 (i-j) * (ai-aj);
    尝试不同的索引差下，最大的目标值
    :param height:
    :return:
    """
    # 以下方法会超时
    # j = len(height) - 1  # 8
    # target_value = -1
    # while j > 0:  # 索引差最大为8，最小为1; 尝试不同的索引差下，最大的目标值 索引差为i时，有9-i个不同的组合
    #     # 有 len(height)-j 个组合
    #     for i in range(0, len(height)-j):  # 循环次数是组合个数
    #         cur = j * min(height[i], height[i+j])
    #         if cur > target_value:
    #             target_value = cur
    #     j -= 1
    # return target_value
    # 重点：向内移动短板才可能增加面积！！！
    j = len(height) - 1
    i = 0
    target = -1
    while i < j:
        cur = (j-i)*min(height[i], height[j])
        if cur > target:
            target = cur
        if height[i] > height[j]:
            j -= 1
        elif height[i] <= height[j]:
            i += 1
    return target


if __name__ == '__main__':
    # height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 8, 100, 2, 100, 4, 8, 3, 7]
    print(maxArea(height))
