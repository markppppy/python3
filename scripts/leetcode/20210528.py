#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210528.py
# @Desc    : 
# @Time    : 2021/5/28 16:20
# @Author  : songpeiyao
# @Version : 1.0


"""
合并两个有序数组
https://leetcode-cn.com/leetbook/read/all-about-array/x9lhe7/

"""
from typing import List


class Solution:

    # def __init__(self):
    #     pass

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        # m 不会等于0
        # nums1每次中间加一个元素，后面的元素位置要加1
        j = n-1
        while j >= 0:
            nums1[j-n] = nums2[j]
            j -= 1
        nums1.sort()
        return

    def merge2(self, nums1, m, nums2, n):

        # 尾插入法
        if (n < 1):
            return
        if (m < 1):
            nums1[0:n] = nums2[0:n]
            return
        k = m + n - 1
        i = m - 1
        j = n - 1

        while k >= 0:
            if (nums1[i] > nums2[j] and i >= 0) or (j < 0 and i >= 0):
                nums1[k] = nums1[i]
                k -= 1
                i -= 1

            if (nums2[j] >= nums1[i] and j >= 0) or (i < 0 and j >=0):
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

    def merge3(self, nums1, m, nums2, n):
        """
        尾插法抄写
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        if n < 1:
            return
        if m < 1:
            nums1[0: n] = nums2[0: n]  # nums2[0: n] 等价于 nums2
            return
        k = m + n - 1  # 因为要保证nums1和nums2合并后有序，所以k为m+n+1；nums1[k]初始是nums1中最后一个元素，用来补位的0
        i = m - 1  # nums1
        j = n - 1  # nums2
        while k >= 0:
            if (nums1[i] > nums2[j] and i >= 0) or (j < 0 and i >= 0):  # i >= 0 是为了防止重复遍历nums1; j < 0 是当nums2中没有元素时，nums1[k] = nums2[i]
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            if (nums1[i] <= nums2[j] and j >= 0) or (i < 0 and j >= 0):
                nums1[k] = nums2[j]
                j -= 1
                k -= 1


nums1 = [1, 2, 4, 5, 6, 0]
m = 5
nums2 = [3]
n = 1

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3


if __name__ == '__main__':
    aa = Solution()
    aa.merge3(nums1, m, nums2, n)
    print(nums1)
