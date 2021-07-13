#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210712.py
# @Desc    : 
# @Time    : 2021/7/12 15:05
# @Author  : songpeiyao
# @Version : 1.0
"""
设计链表

设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val和next。val是当前节点的值，next是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性prev以指示链表中的上一个节点。
假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第index个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为val的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。如果index等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引index 有效，则删除链表中的第index 个节点。

"""


class Node_:  # 不继承 object 可以吗?
    def __init__(self, x):
        self.val = x
        self.next = None  # .next 是一个对象


class MyLinkedList_:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)  # head.val=0, head.next=None
        # self = [{}] ?

    def get(self, index: int) -> int:  # index 等于 0 时, 是什么含义?
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.head
        if index < 0:  # index 是从0开始的
            return -1
        for _ in range(index+1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        _a = Node(val)  # 新增的值怎么定义? 就这样任意初始化一个变量
        _a.next = self.head.next
        self.head.next = _a

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # 从 self.head 一直取到最后
        node = self.head
        while node.next is not None:
            node = node.next  # 怎么取到另一个值?  node.next是一个对象

        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for _ in range(index):
            if node is not None:
                node = node.next
            else:
                return  # If index is greater than the length, the node will not be inserted.
        if node is None:  # 证明index-1位置是尾节点
            node = Node(val)
        else:
            new = Node(val)
            new.next = node.next
            node.next = new

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
        node = self.head
        for _ in range(index):
            if node is not None:
                node = node.next
            else:
                return
        if node.next is not None:  # node 是index-1位置的节点, node.next表示node不是尾结点
            ndel = node.next
            node.next = ndel.next
            ndel.next = None


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# a = Node(2)
# print(a.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 类实例化的时候，会给对象一个属性
        self.head = Node(0)  # Node(0) 表示Node类的实例化

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0: return -1
        node = self.head
        for _ in range(index + 1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new = Node(val)
        new.next = self.head.next
        self.head.next = new

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = self.head
        for i in range(index):
            if node is None:
                return
            node = node.next
        if node is None:
            node = Node(val)
        else:
            new = Node(val)
            new.next = node.next
            node.next = new

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0: return
        node = self.head
        for _ in range(index):
            node = node.next
        if node.next is not None:
            node.next = node.next.next


if __name__ == '__main__':
    a = MyLinkedList()
    print(a.head)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
