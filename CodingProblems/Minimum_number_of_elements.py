# User function Template for python3
class Solution:
    def minCount(self, nums, n):
        # code here
        dp = [[[0 for _ in range(n + 2)] for __ in range(n + 2)] for ___ in range(n + 1)]

        for i in range(n + 1):
            for j in range(1, n + 2):
                for k in range(1, n + 2):
                    if i > 0:
                        dp[i][j][k] = dp[i - 1][j][k]
                        if j == n + 1 or nums[i - 1] < nums[j - 1]:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][i][k] + 1)
                        if k == n + 1 or nums[i - 1] > nums[k - 1]:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][i] + 1)

        return n - dp[n][n + 1][n + 1]


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minCount(arr, n)
        print(ans)

# } Driver Code Ends
