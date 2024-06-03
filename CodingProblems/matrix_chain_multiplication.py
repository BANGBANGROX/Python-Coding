# User function Template for python3

class Solution:
    def __init__(self):
        self.dp = None
        self.nums = None

    def _matrix_multiplication_handler(self, left: int, right: int):
        if left >= right:
            return 0

        if self.dp[left][right] != -1:
            return self.dp[left][right]

        result = 1e9

        for mid in range(left, right):
            result = min(result, self._matrix_multiplication_handler(left, mid) + self._matrix_multiplication_handler(mid + 1, right) + self.nums[left - 1] * self.nums[mid] * self.nums[right])

        self.dp[left][right] = result

        return result

    def matrixMultiplication(self, n: int, nums: list):
        self.nums = nums
        self.dp = [[-1 for _ in range(n)] for __ in range(n)]

        return self._matrix_multiplication_handler(1, n - 1)



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