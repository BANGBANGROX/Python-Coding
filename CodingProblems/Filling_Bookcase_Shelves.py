from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            totalWidth = books[i - 1][0]
            maxHeight = books[i - 1][1]
            dp[i] = dp[i - 1] + maxHeight
            for j in range(i - 1, 0, - 1):
                totalWidth += books[j - 1][0]
                if totalWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + maxHeight)

        return dp[n]
