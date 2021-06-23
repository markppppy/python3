#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210623.py
# @Desc    : 
# @Time    : 2021/6/23 12:45
# @Author  : songpeiyao
# @Version : 1.0
"""
数组拆分 I

给定长度为2n的整数数组 nums ，你的任务是将这些数分成n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到n 的 min(ai, bi) 总和最大。

返回该 最大总和 。

输入：nums = [1,4,3,2]
输出：4
解释：所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4

"""
from typing import List


def arrayPairSum(nums: List[int]) -> int:
    # 题意理解：尽可能让值相近的数字在一起
    # 做法：排序后，把下标为偶数元素相加; so easy
    nums.sort()
    n = len(nums)
    target = 0
    if n == 0:
        return target
    for i in range(n//2):
        target += nums[i*2]
    return target


if __name__ == '__main__':
    print()

