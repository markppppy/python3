#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210720.py
# @Desc    : 
# @Time    : 2021/7/20 9:44
# @Author  : songpeiyao
# @Version : 1.0
"""
删除链表的倒数第N个节点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

进阶：你能尝试使用一趟扫描实现吗？
"""
import collections
from Cython.Compiler.ExprNodes import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 记录头结点和第二节点，当走完时, 结合n判断删除的是哪个节点; 如果删除的是头结点就返回第二节点，如果不是，就返回第二结点；
        # 上述方法没有删除结点。。。要在从头结点走一遍才能删结点，怎么满足进阶的要求? 把每个node保存到list中? 或者 dict中, key为顺序?
        node = head
        dct = {}
        i = 1
        while node is not None:
            dct[i] = node
            i += 1
            node = node.next
        ni = i - n
        try:
            dct[ni-1].next = dct[ni].next
            dct[ni].next = None
        except:
            head = dct[ni].next
        return head


if __name__ == '__main__':
    print()
