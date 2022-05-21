from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = int(1e9) + 5
        dp = [inf] * (amount + 1)

        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if coin > amt:
                    continue
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        if dp[amount] == inf:
            return -1

        return dp[amount]
