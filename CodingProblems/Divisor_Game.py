class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)  # Losing state -- False Winning state -- True

        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0:
                    if dp[i - j] == True:
                        dp[i] = True
                        break

        return dp[n]

       # Or simply
       # return n % 2 == 0 :)
