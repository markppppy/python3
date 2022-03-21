#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210624.py
# @Desc    : 
# @Time    : 2021/6/24 12:48
# @Author  : songpeiyao
# @Version : 1.0
"""
长度最小的子数组

给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

[1,2,3,4,5]  11

6
[10,2,3]
"""
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    min_len = n+1
    i, j = 0, 0
    while j <= n-1:
        if sum(nums[i: j+1]) < target:
            j += 1
        elif sum(nums[i: j+1]) >= target:
            min_len = min(min_len, len(nums[i: j+1]))
            i += 1

    if min_len == n+1:
        return 0
    return min_len


if __name__ == '__main__':
    target = 6
    nums = [10, 2, 3]
    print(minSubArrayLen(target, nums))
    # print(len(nums[1: 2]))
