from typing import List


class Solution:
    dp = []
    ones = []
    zeroes = []

    def findMaxFormUtil(self, strs: List[str], m: int, n: int, ind: int) -> int:
        if ind == len(strs):
            return 0

        if self.dp[ind][m][n] != -1:
            return self.dp[ind][m][n]

        ans = 0

        # Take the current string if possible
        if self.zeroes[ind] <= m and self.ones[ind] <= n:
            ans = self.findMaxFormUtil(
                strs, m - self.zeroes[ind], n - self.ones[ind], ind + 1) + 1

        # Leave the current string
        ans = max(ans, self.findMaxFormUtil(strs, m, n, ind + 1))

        self.dp[ind][m][n] = ans

        return ans

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        self.dp = [[[-1] * (n + 1) for i in range(m + 1)]
                   for i in range(length)]
        self.zeroes = [0] * length
        self.ones = [0] * length

        for i in range(length):
            onesCount = 0
            zeroesCount = 0
            s = strs[i]
            for ch in s:
                if ch == '0':
                    zeroesCount += 1
                else:
                    onesCount += 1
            self.ones[i] = onesCount
            self.zeroes[i] = zeroesCount

        return self.findMaxFormUtil(strs, m, n, 0)
