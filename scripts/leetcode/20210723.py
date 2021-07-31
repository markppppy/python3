#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210723.py
# @Desc    : 
# @Time    : 2021/7/23 10:02
# @Author  : songpeiyao
# @Version : 1.0
"""
回文链表

请判断一个链表是否为回文链表。
输入: 1->2->2->1
输出: true
1 2 3 4 54  23  1  fast.next is none

1 2 3 4 5 6  65  43  21    fast is none

1 2  1
1 2
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

? 自己写的解法是O(n) 空间复杂度，怎么优化为O(1) ?
"""
from Cython.Compiler.ExprNodes import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
           1. 用 快慢指针 确定链表中心位置，中心位置可能是一个节点也可能是两个节点
           2. 中心位置的前半部分从头结点遍历，中心位置后半部分从中心节点的下一个节点开始遍历

           实际编程耗时点: 1. 找中心位置时fast的判断; 2. 在给dct赋值时，step被修改了，导致最后判断是否为回文链表时，再用到step就一直判断错误
        """
        # 边界情况
        if head.next is None:  # 链表长度为1
            return True
        if head.next.next is None:  # 链表长度为2
            if head.val == head.next.val:
                return True
            else:
                return False
        # 1. 用 快慢指针 确定链表中心位置，中心位置可能是一个节点也可能是两个节点
        center_node_num = None
        fast = slow = head
        step = 0  # 记录slow走的步数
        # fast.next is None 中心节点是一个;  fast最后一次走的时候，第二步是None 中心节点是两个: 因为慢指针走到第二个中心节点时，快指针总是走的慢指针步数2倍，但实际链表长度已经不够了
        while fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
            else:
                center_node_num = 2
                break
            slow = slow.next
            step += 1
        if center_node_num is None:
            center_node_num = 1

        # 让 slow 把后半部分走完，并把后半部分的节点保存在 dict 中; 以下判断不适合 链表长度为 1,2 的情况
        dct = {}
        tmp_step = step
        if center_node_num == 1:
            dct[tmp_step] = slow
            tmp_step -= 1
        while tmp_step >= 0:
            dct[tmp_step] = slow.next
            slow = slow.next
            tmp_step -= 1
        # 从链表两端判断是否是回文链表
        slow = head
        n = 0
        while n <= step:
            if slow.val == dct[n].val:
                n += 1
                slow = slow.next
                continue
            else:
                return False
        return True


