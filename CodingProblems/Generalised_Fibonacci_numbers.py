# User function Template for python3

class Solution:
    def multiply(self, a, b, MOD):
        n = len(a)
        ans = [[0 for _ in range(n)] for __ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ans[i][j] = (ans[i][j] + (a[i][k] * b[k][j]) % MOD) % MOD

        for i in range(n):
            for j in range(n):
                a[i][j] = ans[i][j]

    def matrixExponentiation(self, ans, a, b, n, m):
        startingMatrix = [[a, b, 1], [1, 0, 0], [0, 0, 1]]

        while n > 0:
            if n % 2 == 1:
                self.multiply(ans, startingMatrix, m)
                n -= 1
            self.multiply(startingMatrix, startingMatrix, m)
            n >>= 1

    def genFibNum(self, a, b, c, n, m):
        # code here
        if n <= 2:
            return int(1 % m)

        ans = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        self.matrixExponentiation(ans, a, b, n - 2, m)

        return (ans[0][0] + ans[0][1] + ans[0][2] * c) % m

        # {
     # Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, n, m = map(int, input().split())

        ob = Solution()
        print(ob.genFibNum(a, b, c, n, m))
# } Driver Code Ends
