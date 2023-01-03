# User function Template for python3

class Solution:
    def compute_value(self, n):
        # Code here
        ans = 1
        MOD = int(1e9 + 7)

        for i in range(1, n + 1):
            ans *= (n + i)
            ans //= i

        return int(ans % MOD)


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.compute_value(n)
        print(ans)
# } Driver Code Ends
