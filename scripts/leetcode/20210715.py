#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210715.py
# @Desc    : 
# @Time    : 2021/7/15 16:33
# @Author  : songpeiyao
# @Version : 1.0
"""
环形链表 II

给定一个链表，返回链表开始入环的第一个节点。如果链表无环，则返回null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

提示：
链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引

逻辑分析：
FAST 每次比 SLOW 多走一步；
如果不存在环，FAST将最先到达尾节点；
当存在环：
设头节点到到环的入口点
当FAST和SLOW第一次相遇

"""
import collections
from Cython.Compiler.ExprNodes import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        dct = collections.defaultdict(int)
        fast = slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return fast
        return None


if __name__ == '__main__':
    print()
