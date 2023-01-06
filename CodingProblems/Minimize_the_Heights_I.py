# User function Template for python3

class Solution:
    def getMinDiff(self, heights, n, k):
        # code here
        heights.sort()

        ans = heights[n - 1] - heights[0]

        for i in range(1, n):
            maxValue = max(heights[i - 1] + k, heights[n - 1] - k)
            minValue = min(heights[0] + k, heights[i] - k)
            ans = min(ans, maxValue - minValue)

        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
