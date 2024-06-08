# User function Template for python3

class Solution:
    def __init__(self):
        self.nums: list = list()
        self.n: int = 0
        self.dp: list = list()

    def _lower_bound(self, key: int) -> int:
        left = 0
        right = self.n - 1

        while left <= right:
            mid = (left + ((right - left) >> 1))
            if self.dp[mid] >= key:
                right = mid - 1
            else:
                left = mid + 1

        return left

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n: int, nums: list) -> int:
        self.dp = []
        self.nums = nums
        self.n = n
        size = 0

        self.dp.append(nums[0])
        size += 1

        for i in range(1, n):
            if nums[i] > self.dp[size - 1]:
                self.dp.append(nums[i])
                size += 1
            else:
                self.dp[self._lower_bound(nums[i])] = nums[i]

        return size

# code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.longestSubsequence(n, a))

# } Driver Code Ends