#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project : DataMachine_for_timers
# @File    : 20210529.py
# @Desc    : 
# @Time    : 2021/5/29 15:03
# @Author  : songpeiyao
# @Version : 1.0
from typing import List


class Solution:
    """
    给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target

    输入：numbers = [2,7,11,15], target = 9
    输出：[1,2]
    解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

    可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 思路：头部定义一个指针，尾部定义一个指针，每次头部指针不动，移动尾部指针，然后移动头部指针后，再次移动尾部指针; 超时，方法需要优化
        # for i in range(len(numbers)):
        #     for g in range(i, len(numbers)):
        #         if numbers[i] + numbers[g] == target:
        #             return [i+1, g+1]
        # 利用numbers有序减少了遍历次数
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        s = s.lower()
        lst = list(s)
        # 删除lst中的空格
        new_lst = []
        for l in lst:
            if l.isalnum():
                new_lst.append(l)
        n = len(new_lst) // 2
        for ni in range(n):
            if new_lst[ni] != new_lst[-(ni + 1)]:
                return False
        return True

    def reverseVowels(self, s: str) -> str:
        """
        交换字符串中的元音字母
        """
        # 元音字母: a e i o u
        target = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'o', 'u']
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() is False:
                i += 1
                continue
            if s[j].isalnum() is False:
                j -= 1
                continue
            if s[i] in target and s[j] in target:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in target and s[j] not in target:
                j -= 1
            elif s[i] not in target and s[j] in target:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    # numbers = [2, 7, 11, 15]
    # target = 9

    # result = s.twoSum(numbers, target)
    # print(result)

    # st = "A man, a plan, a canal: Panama"
    # print(s.isPalindrome(st))

    # st = "hello"
    st = "aA"
    print(s.reverseVowels(st))
