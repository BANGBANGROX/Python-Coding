# User function Template for python3

class Solution:
    def TotalWays(self, n):
        # Code here
        if n == 1:
            return 4

        if n == 2:
            return 9

        dp = [0 for _ in range(n+1)]
        mod = int(1e9 + 7)

        dp[1] = 2
        dp[2] = 3

        for i in range(3, n+1):
            dp[i] = (dp[i-1]+dp[i-2]) % mod

        return (dp[n] * dp[n]) % mod
# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.TotalWays(N)
        print(ans)
# } Driver Code Ends
