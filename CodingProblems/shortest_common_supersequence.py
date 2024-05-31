class Solution:
    def __init__(self):
        self.s1 = None
        self.s2 = None

    def _get_lcs(self) -> str:
        m = len(self.s1)
        n = len(self.s2)
        dp = [["" for _ in range(n + 1)] for __ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.s1[i - 1] == self.s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + self.s1[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][
                        j - 1]

        return dp[m][n]

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        self.s1 = str1
        self.s2 = str2
        lcs = self._get_lcs()
        m = len(str1)
        n = len(str2)
        i = 0
        j = 0
        answer = ""

        for ch in lcs:
            while i < m and str1[i] != ch:
                answer += str1[i]
                i += 1
            while j < n and str2[j] != ch:
                answer += str2[j]
                j += 1
            answer += ch
            i += 1
            j += 1

        answer += (str1[i:] + str2[j:])

        return answer
