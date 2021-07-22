#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210721.py
# @Desc    : 
# @Time    : 2021/7/21 17:54
# @Author  : songpeiyao
# @Version : 1.0
"""
移除链表元素

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

"""
from Cython.Compiler.ExprNodes import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        node = head
        real_head = head
        pre_node = None
        while node is not None:
            if node.val == val:
                if pre_node is None:
                    real_head = node.next
                    if real_head is None:
                        return real_head
                else:
                    pre_node.next = node.next
            else:
                pre_node = node
            node = node.next
        return real_head

"""
奇偶链表

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

思路: 第一个节点为奇节点的头节点even, 第二个节点是偶节点的头节点odd, 

odd.next = even.next
odd = odd.next
even.next = odd.next
even = even.next

如果 even 或 even.next 是 None , 停止循环

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = oddHead = head
        even = evenHead = head.next

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            # 已知 even.next 即 odd 不为None
            even.next = odd.next
            even = even.next
        odd.next = evenHead

        return oddHead





