

"""
451. 根据字符出现频率排序

给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。


645. 错误的集合

集合 s 包含从 1 到n的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

感想：因为645是简单题，又因为没有看清题目问题和难点，导致提交了10次都还在错误，心态崩了
"""

from collections import Counter, defaultdict
from typing import List


def frequencySort(s: str) -> str:
    # 我的写法
    # 定义字典d 维护每个字母的出现次数，计算字母出现次数时，把其删掉，减少后面字母的查找次数；当s中的字母已经在d中，就不会再次计算
    d = defaultdict(int)
    target = []
    lst = list(s)
    if len(s) < 2:
        return s

    for _ in range(len(s)):
        d[lst[0]] += 1
        lst.pop(0)

    # 字典按values排序
    d_order = sorted(d.items(), key=lambda kv: kv[1], reverse=True)  # (kv[1], kv[0])

    for t in d_order:
        for _ in range(t[1]):
            target.append(t[0])
    return ''.join(target)


def frequencySort_oth(s: str) -> str:
    # python中更简洁的写法, 或者用 Counter().most_common()
    c = Counter(s)
    # sorted 的 key可以调整排序的顺序
    """The value of the key parameter should be a function (or other callable) that takes a single argument and 
    returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once 
    for each input record. """
    # -c[x] 是因为sorted默认升序排序，而我们希望是按照出现频率降序排
    a = sorted(c.keys(), key=lambda x: -c[x])
    result = ""
    for i in a:
        result += i * c[i]
    return result


def findErrorNums(nums: List[int]) -> List[int]:
    # 找出重复出现的整数，再找到丢失的整数
    # nums中包含了1到n, n=len(nums), 先找出重复的数，再找出缺失的数，方法分别是？！

    n = len(nums)
    nums.sort()

    i, j = 0, 0
    dup = -1
    drop = -1
    while i < n-1:
        if nums[i] == nums[i+1]:
            dup = nums[i]
        i += 1
    if max(nums) != n:
        return [dup, n]
    elif min(nums) != 1:
        return [dup, 1]

    while j < n-1:
        if nums[j+1] - nums[j] == 2:
            drop = nums[j] + 1
            break
        j += 1
    return [dup, drop]


if __name__ == '__main__':
    print()
    s = "tree"
    c = Counter(s)  # Counter({'e': 2, 't': 1, 'r': 1})   c.keys()  dict_keys(['t', 'r', 'e']
    print(c, c.keys())
    # 错误的集合
    lst = [37, 62, 43, 27, 12, 66, 36, 18, 39, 54, 61, 65, 47, 32, 23, 2, 46, 8, 4, 24, 29, 38, 63, 39, 25, 11, 45, 28,
           44, 52, 15, 30, 21, 7, 57, 49, 1, 59, 58, 14, 9, 40, 3, 42, 56, 31, 20, 41, 22, 50, 13, 33, 6, 10, 16, 64,
           53, 51, 19, 17, 48, 26, 34, 60, 35, 5]
    print(findErrorNums(lst))
