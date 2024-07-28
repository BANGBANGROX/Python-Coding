class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for str_len in range(2, n + 1):
            for i in range(0, n - str_len + 1):
                j = i + str_len - 1
                if s[i] == s[j]:
                    low = i + 1
                    high = j - 1
                    while low <= high and s[i] != s[low]:
                        low += 1
                    while low <= high and s[j] != s[high]:
                        high -= 1
                    if low > high:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 2) % MOD
                    elif low == high:
                        dp[i][j] = (dp[i + 1][j - 1] * 2 + 1) % MOD
                    else:
                        dp[i][j] = (
                            dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1] + MOD
                        ) % MOD
                else:
                    dp[i][j] = (
                        dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + MOD
                    ) % MOD

        return dp[0][n - 1]


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        print(Solution().countPalindromicSubsequences(s=input()))
