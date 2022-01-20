#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Directory: D:\Document\local_rps\python3\scripts\leetcode
# @File     : 20220119.py
# @Time     : 2022/01/19 13:35:08
# @Author   : songpeiyao 
# @Version  : 1.0
# @Contact  : ppppy161@qq.com
# @Desc     : None

"""
219. 存在重复元素 II

给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

输入：nums = [1,2,3,1], k = 3
输出：true

输入：nums = [1,0,1,1], k = 1
输出：true

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
"""


def get_result():
    nums = [1,2,3,1]
    k = 3
    # 思路1: 遍历; 因为是判断是否存在，所以满足条件就能返回; 感觉也只有这一个方法; 超时; 
    # lth = len(nums)
    # if lth < 2:
    #     return False 
    # for i in range(lth):
    #     for j in range(i+1, min(i+k+1, lth)):
    #         if nums[i] == nums[j]:
    #             return True 
    # return False 
    
    # 思路2: 维护一个长度为k的数组; 有提升，但是在最后一个测试用例超时；时间复杂度不是O(n)，应该是 nums[i] in target 这个判断有问题, 但是加了 target = set(target) 还是超时。。。
    # todo 
    # lth = len(nums)
    # if lth < 2:
    #     return False 
    # for i in range(lth):
    #     target = nums[i+1: min(i+1+k, lth)]
    #     target = set(target)
    #     if nums[i] in target:
    #         return True 
    # return False 

    # 滑动窗口，相比思路2，num in s 利用了哈希表的优势
    s = set()
    for i, num in enumerate(nums):
        if i > k:
            s.remove(nums[i-k-1]) 
        if num in s:
            return True 
        else:
            s.add(num)
    return False 


print(get_result())







