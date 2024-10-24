# User function Template for python3


class Solution:
    def maxProfit(self, k: int, n: int, prices: list[int]) -> int:
        # code here
        dp: list[int] = [[0 for _ in range(n)] for _ in range(k + 1)]
        INF: int = 10**9

        for i in range(1, k + 1):
            price_diff = -1 * INF
            for j in range(1, n):
                price_diff = max(price_diff, dp[i - 1][j - 1] - prices[j - 1])
                dp[i][j] = max(dp[i][j - 1], price_diff + prices[j])

        return dp[k][n - 1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t: int = int(input())
    for _ in range(t):
        K: int = int(input())
        N: int = int(input())
        A: int = input().split()
        for i in range(N):
            A[i] = int(A[i])

        ob = Solution()
        print(ob.maxProfit(K, N, A))
        print("~")
# } Driver Code Ends
