
#  arr diff 最长等差子序列长度
'''
方法1: 从arr第一个元素遍历，以每个元素作为子序列第一个元素，看 +diff后的元素是否在剩下的列表中，如果在，就以第二个元素为基数，+diff看是否在后续的列表中，一次类推。
如果结束，以arr第二个元素为子序列第一个元素，重复上述过程。

'''

from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lth = len(arr)
        max_sub_lst_lth = 1
        for i in range(lth):
            l = i  # l 为 arr 的下标
            sub_lst_lth = 1
            while l < lth-1:
                if arr[l] + difference in arr[l+1: ]:
                    l = arr[l+1: ].index(arr[l] + difference) + len(arr[: l+1])
                    sub_lst_lth += 1
                else:
                    break
            max_sub_lst_lth = max(max_sub_lst_lth, sub_lst_lth)
        return max_sub_lst_lth

    def longestSubsequence_qp(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for v in arr:
            dp[v] = dp[v-difference] + 1
        return max(dp.values())




# arr = [1, 2, 3, 4]
# print(arr[:1])
# arr = [1, 3, 5, 7]
# arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
arr = [4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8]
difference = 0
print(Solution().longestSubsequence_qp(arr, difference))
