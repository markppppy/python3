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


"""
两数之和 II - 输入有序数组

给定一个已按照 升序排列的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。


输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

"""


def twoSum(numbers: List[int], target: int) -> List[int]:
    # 老题重做
    n = len(numbers)
    i = 0
    j = n - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] > target:
            j += 1
        elif numbers[i] + numbers[j] < target:
            i += 1
    # return []


"""
最大连续1的个数
给定一个二进制数组， 计算其中最大连续 1 的个数。

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
"""


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    # 难点在边界值的考虑
    max_len = 0
    ln = len(nums)
    i, j = -1, -1
    # i, j初始化
    for n in range(ln):
        if nums[n] == 1:
            i, j = n, n
            break
    if i == -1:
        return 0
    while j <= ln-1:
        if nums[j] != 1:
            # 计算i到j的长度
            if nums[i] == 1:
                max_len = max(max_len, j-i)
                i = j
            if j+1 <= ln-1 and nums[j+1] == 1:
                i = j+1
            # max_len =
            j += 1
        elif j == ln-1:
            if nums[i] == 1:
                max_len = max(max_len, j-i+1)
            j += 1
        else:
            j += 1

    return max_len


if __name__ == '__main__':
    input_nums = [1, 1, 0, 1, 1, 1]
    print(findMaxConsecutiveOnes(input_nums))
    print()

