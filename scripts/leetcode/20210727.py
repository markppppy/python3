#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210727.py
# @Desc    : 
# @Time    : 2021/7/27 12:34
# @Author  : songpeiyao
# @Version : 1.0
"""
设计循环队列

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = -1  # 初始化tail的定义很重要, 之前是定为0了, 但应该定为-1
        self.length = k
        self.spare = k   # 多定义了这个变量，代码简化了很多
        self.space = [0]*k

    def enQueue(self, value: int) -> bool:
        # 每次增加元素是加在尾部的!
        # 判断 head 到 tail 的距离和 length 的大小
        # tail 在 head 前面
        # tail 在 head 后面
        # if self.tail < self.head:
        #     spare = self.length - (self.tail + self.length - self.head + 1)
        # else:
        #     spare = self.length - (self.head - self.tail + 1)
        if self.spare > 0:  # self.head == self.tail 可能是空也可能是满
            self.tail += 1
            self.tail = (self.tail+1) % self.length - 1
            self.space[self.tail] = value
            self.spare -= 1
        else:
            return False
        return True

    def deQueue(self) -> bool:
        # 只要self.head != self.tail就可以删除，问题是 self.head 怎么移动
        if self.spare != self.length:
            self.head += 1
            self.head = (self.head+1) % self.length - 1
            self.spare += 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.spare < self.length:
            return self.space[self.head]
        else:
            return -1

    def Rear(self) -> int:
        if self.spare < self.length:
            return self.space[self.tail]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.spare == self.length:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.spare == 0:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
