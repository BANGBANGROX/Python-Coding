# User function Template for python3


class Solution:
    def LongestRepeatingSubsequence(self, s: str) -> int:
        # Code here
        n: int = len(s)
        dp: list[list[int]] = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j] and i != j:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]             


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T: int = int(input())
    for i in range(T):
        s: str = input()
        ob: Solution = Solution()
        ans: int = ob.LongestRepeatingSubsequence(s)
        print(ans)

# } Driver Code Ends
