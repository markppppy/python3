#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @Directory: D:\Document\local_rps\python3\scripts\algoxy
# @File     : min_free_num.py
# @Time     : 2021/11/17 10:23:39
# @Author   : songpeiyao 
# @Version  : 1.0
# @Contact  : ppppy161@qq.com
# @Desc     : 一串数字中找出没有出现的最小数字

"""
思路1: 从0开始，每次遍历数组lst，看n是否在lst中，如果在 n = n + 1, 如果不在，返回n; 
优点: 很直观的想法，好理解；
缺点: 时间复杂度为O(n^2)

思路2: 对目标数组lst排序，遍历lst, 下标i如果不等于对应元素a, 则返回i+1即为没有出现的最小数字;
缺点: 时间复杂度=排序方法的时间复杂度

思路3: lth = len(lst), lst的最小元素一定小于等于lth;  
      初始化一个长度为 lth+1 的全为 False 数组 target，遍历lst中的元素，如果小于等于lth, target下标对应位置改为True(!);
      遍历target, 返回第一个False的下标; 
优点: 时间复杂度为O(n)

思路4: 分治法; 把lst分为a和b两个集合，a中保存小于等于 floor(n/2) 的元素，如果a的长度等于 floor(n/2), 则目标值一定在b中，然后对b执行相同操作；

"""

target_lst = [10, 1, 2, 6, 7, 3, 8, 8, 4, 5]  # 结果应为: 9, 假设最小元素不包含0

def get_min_num_1(lst):
    for i in range(1, len(lst)+2):
          if i in lst:
              continue
          else:
              return i 

def get_min_num_2(lst):
    ordered_lst = sorted(set(lst), reverse=False)
    for i in range(len(ordered_lst)):
          if i != ordered_lst[i] - 1:
                return i + 1
    return len(ordered_lst) + 1

def get_min_num_3(lst):
    lth = len(lst)
    sub_lst = [False] * (lth + 1)  
    for i in range(lth):
        if lst[i] <= lth:
              sub_lst[lst[i]-1] = True  # 因为自己假设的最小元素不包含0，所以比较复杂 
    for i in range(lth + 1):
        if sub_lst[i] == False:
            return i + 1

def get_min_num_4():
      return 


print(get_min_num_1(target_lst))

