#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210602.py
# @Desc    : 
# @Time    : 2021/6/2 9:44
# @Author  : songpeiyao
# @Version : 1.0
from typing import List
"""
给定一个含有n个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
"""


def minSubArrayLen(target: int, nums: List[int]) -> int:
    # 定义两个指针i j;
    # i不动，j增加，当i~j的和大于等于target时，j不在变，记录长度；
    # i+1，。。。
    # 循环
    i = 0
    j = 0
    minlen = len(nums)+1
    while i < len(nums):
        while j < len(nums):
            if sum(nums[i: j+1]) >= target:
                minlen = min(minlen, j-i+1)
                break
            j += 1
        i += 1
    if minlen == len(nums)+1:
        minlen = 0
    return minlen


def minSubArrayLen2(s, nums):
    """
    相比 minSubArrayLen 减少不必要的遍历
    :type s: int
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)
    if n < 1 or sum(nums) < s:
        return 0

    # 维护一个滑动窗口nums[i,j], nums[i...j] < s
    i = 0
    j = -1
    total = 0
    res = n + 1
    while i <= n-1:
        if (j + 1 < n) and total < s:
            j += 1
            total += nums[j]
        else:
            total -= nums[i]
            i += 1

        if total >= s:
            res = min(res, j-i+1)
    if res == n+1:
        return 0
    return res


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(minSubArrayLen2(target, nums))
