# User function Template for python3

class Solution:
    def posIntSol(self, s):
        # code here
        n = 1
        equalIndex = -1

        for i in range(len(s)):
            if s[i] == '=':
                equalIndex = i
                break
            if s[i] == '+':
                n += 1

        k = int(s[equalIndex+1:])
        ans = 1

        for i in range(1, n):
            ans *= (k - i)
            ans //= i

        return ans

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.posIntSol(s))
# } Driver Code Ends
