# User function Template for python3

class Solution:
    def matrixMultiplication(self, n: int, sizes: list):
        dp = [[0 for _ in range(n)] for __ in range(n)]

        for left in range(n - 1, 0, -1):
            for right in range(left + 1, n):
                dp[left][right] = 1e9
                for mid in range(left, right):
                    dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid + 1][right] + sizes[left - 1] * sizes[mid] * sizes[right])

        return dp[1][n - 1]


# code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends