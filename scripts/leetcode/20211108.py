class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 返回: nAmB, n是数字和位置都对的个数, m是数字对但位置不对的个数
        # 思路: 一次循环判断n的大小，改变 guess 后，一次循环判断m大小
        lst = [] 
        n = m = 0 
        secret = list(secret)
        guess = list(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                n += 1
                secret[i] = 'A'
            else:
                lst.append(guess[i])
        # lst = list(set(lst))
        for i in range(len(lst)):
            if lst[i] in secret:
                m += 1
                secret[secret.index(lst[i])] = 'B'
        return '%dA%dB'%(n, m)


secret = "1807"
guess = "7810"
print(Solution().getHint(secret, guess))