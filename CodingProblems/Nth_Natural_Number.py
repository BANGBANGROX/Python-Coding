# User function Template for python3

class Solution:
    def findNth(self, n):
        # code here
        ans = ""

        while n > 0:
            ans += str(n % 9)
            n //= 9

        return ans[::-1]

        # {
     # Driver Code Starts
        # Initial Template for Python 3


t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)
# } Driver Code Ends
