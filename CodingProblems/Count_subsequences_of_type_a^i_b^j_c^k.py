# User function Template for python3

class Solution:
    def fun(self, s):
        # code here
        a = 0
        ab = 0
        abc = 0
        mod = int(1e9 + 7)

        for ch in s:
            if ch == 'a':
                a = (2 * a + 1) % mod
            elif ch == 'b':
                ab = (2 * ab + a) % mod
            else:
                abc = (2 * abc + ab) % mod

        return abc

# {
#  Driver Code Starts
# Initial Template for Python 3

# Position this line where user code will be pasted.


t = int(input())
for _ in range(t):
    s = input()
    print(Solution().fun(s))
# } Driver Code Ends
