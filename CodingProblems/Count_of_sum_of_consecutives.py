# User function Template for python3
import math


class Solution:
    def getCount(self, n):
        # code here
        ans = 0

        for i in range(1, int(math.sqrt(2 * n)) + 1):
            val = n - i * (i - 1) // 2
            if val % i == 0:
                ans += 1

        return ans - 1


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.getCount(N))
# } Driver Code Ends
