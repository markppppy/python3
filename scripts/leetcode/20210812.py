"""
最长回文子序列

给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

acfvfsvaca

s 仅由小写英文字母组成

# 动态规划： 完全超出知识范畴....
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    s = "bbbab"
    s_example = Solution()
    s_example.longestPalindromeSubseq(s)
    print()


