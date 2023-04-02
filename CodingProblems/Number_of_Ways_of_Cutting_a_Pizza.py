from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m = len(pizza)
        n = len(pizza[0])
        apples = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        dp = [[[0 for _ in range(n)] for __ in range(m)] for ___ in range(k)]
        MOD = 10 ** 9 + 7

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] = (1 if ord(pizza[i][j]) == ord('A') else 0) + \
                               apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
                dp[0][i][j] = 1 if apples[i][j] > 0 else 0

        for remain in range(1, k):
            for row in range(m):
                for col in range(n):
                    for next_row in range(row + 1, m):
                        if apples[row][col] - apples[next_row][col] > 0:
                            dp[remain][row][col] = (dp[remain][row][col] +
                                                    dp[remain - 1][next_row][col]) % MOD
                    for next_col in range(col + 1, n):
                        if apples[row][col] - apples[row][next_col] > 0:
                            dp[remain][row][col] = (dp[remain][row][col] +
                                                    dp[remain - 1][row][next_col]) % MOD

        return dp[k - 1][0][0]


if __name__ == "__main__":
    m = int(input())
    pizza = ["" for _ in range(m)]
    for i in range(m):
        pizza[i] = input()
    k = int(input())

    solution = Solution()
    print(solution.ways(pizza, k))
