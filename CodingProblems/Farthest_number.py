# User function Template for python3

class Solution:
    def search(self, nums, l, r, key):
        ans = -1

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if nums[mid] < key:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

    def farNumber(self, n, nums):
        # code here
        ans = [-1] * n
        dp = [-1] * n

        ans[n - 1] = -1
        dp[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            index = self.search(dp, i + 1, n - 1, nums[i])
            ans[i] = index
            dp[i] = min(dp[i + 1], nums[i])

        return ans
        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N = int(input())
        Arr = [int(x) for x in input().split()]

        ob = Solution()
        ans = ob.farNumber(N, Arr)

        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
