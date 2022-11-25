# User function Template for python3

class Solution:
    def longestPerfectPiece(self, nums, n):
        # code here
        i = 0
        j = 0
        ans = 0

        while i < n:
            if abs(nums[i] - nums[j]) <= 1:
                ans = max(ans, i - j + 1)
                i += 1
            else:
                while abs(nums[i]-nums[j]) > 1:
                    j += 1

        return ans
        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.longestPerfectPiece(arr, N))
# } Driver Code Ends
