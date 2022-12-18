# User function Template for python3

import math


class Solution:
    def calculateGCD(self, a, b):
        if b == 0:
            return a

        return self.calculateGCD(b, a % b)

    def maxGcd(self, n):
        # code here\
        ans = 1
        cnt = 0

        while n > 0:
            if self.calculateGCD(ans, n) == 1:
                ans *= n
                cnt += 1
            if cnt == 4:
                return ans
            n -= 1

        return ans

        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = (int)(input())
        ob = Solution()
        print(ob.maxGcd(N))
# } Driver Code Ends
