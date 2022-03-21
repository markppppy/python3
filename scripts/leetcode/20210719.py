#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210719.py
# @Desc    : 
# @Time    : 2021/7/19 18:36
# @Author  : songpeiyao
# @Version : 1.0
"""
相交链表

给你两个单链表的头节点headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
图示两个链表在节点 c1 开始相交：

题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

"""
import collections
from Cython.Compiler.ExprNodes import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dct = collections.defaultdict(int)  # int 默认是0
        head1 = headA
        while head1:
            dct[head1] += 1
            head1 = head1.next
        head2 = headB
        while head2:
            dct[head2] += 1
            if dct[head2] > 1:
                return head2
            head2 = head2.next

# 进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
"""
设A链表长度为a, B链表长度为b, 公共部分为c, 第一个公共节点为node
指针1: A走完走B, 再次走到node时, 走了 a+b-c
指针2: B走完走A, 再次走到node时, 走了  b+a-c
即，当两指针相遇, 一定是第二次走到了 node 
"""
