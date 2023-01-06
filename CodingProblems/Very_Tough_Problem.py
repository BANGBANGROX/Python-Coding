# User function Template for python3

class Solution:
    def toughProblem(self, n, s, x):
        # code here
        ans = ["Yes", "No"]

        if s < x or (s + x) % 2 == 1:
            return ans[1]

        if n == 1:
            return ans[0] if s == x else ans[1]

        if n == 2:
            j = (s - x) // 2

            for bit in range(30, -1, -1):
                if (j & (1 << bit)) > 0:
                    if (x & (1 << bit)) > 0:
                        return ans[1]

        return ans[0]
# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        N, S, X = map(int, input().split())
        print(ob.toughProblem(N, S, X))


# } Driver Code Ends
