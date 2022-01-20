#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Directory: D:\Document\local_rps\python3\scripts\leetcode
# @File     : 20220118.py
# @Time     : 2022/01/18 11:12:34
# @Author   : songpeiyao 
# @Version  : 1.0
# @Contact  : ppppy161@qq.com
# @Desc     : None

"""
539. 最小时间差
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
"""

# 0、因为数组中时间单位是分钟，如果数组长度超过1440，那一定会有两个相同的元素，直接返回0；(边界值)
# 1、写出计算字符串时间的差值的方法；
# 2、排序: 排序用内置方法
# 3、计算相邻元素和收尾元素的时间差

def get_answer():

    timePoints = ["00:00","23:59","00:00"]
    
    lth = len(timePoints)
    
    if lth > 1440: 
        return 0
     
    def get_diff_min(t1, t2):
        h = int(t1[:2]) - int(t2[:2])
        m = int(t1[3:]) - int(t2[3:])
        return h*60 + m 
    
    timePoints.sort()
    
    diff_m = 1441

    for i in range(lth-1):
        diff_m = min(diff_m, -get_diff_min(timePoints[i], timePoints[i+1]))

    diff_m = min(diff_m, 1440 + get_diff_min(timePoints[0], timePoints[-1]))

    return diff_m

print(get_answer())

"""
382. 链表随机节点

给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 被选中的概率一样 。

实现 Solution 类：

Solution(ListNode head) 使用整数数组初始化对象。
int getRandom() 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。

输入
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
输出
[null, 1, 3, 2, 2, 3]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        return 

    def getRandom(self) -> int:
        return 

# todo

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()