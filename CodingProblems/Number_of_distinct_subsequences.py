# User function Template for python3

class Solution:
    def distinctSubsequences(self, s):
        # code here
        n = len(s)
        MOD = 1e9 + 7
        dp = [0 for _ in range(n + 1)]
        index = {}

        dp[0] = 1

        for i in range(1, n + 1):
            ch = s[i - 1]
            dp[i] = (dp[i - 1] * 2) % MOD
            if ch in index:
                idx = index[ch]
                dp[i] = (dp[i] - dp[idx - 1] + MOD) % MOD
            index[ch] = i

        return dp[n]

        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.distinctSubsequences(s)
        print(answer)

# } Driver Code Ends
