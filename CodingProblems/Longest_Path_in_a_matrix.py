# User function Template for python3

class Solution:
    def dfs(self, matrix, x, y):
        if self.dp[x][y] != -1:
            return self.dp[x][y]

        ans = 0

        for i in range(4):
            newX = x + self.dx[i]
            newY = y + self.dy[i]
            if newX >= 0 and newY >= 0 and newX < self.m and newY < self.n and matrix[newX][newY] > matrix[x][y]:
                ans = max(ans, self.dfs(matrix, newX, newY))

        # print(str(x) + " " + str(y) + " " + str(ans))

        self.dp[x][y] = ans + 1

        return self.dp[x][y]

    def longestIncreasingPath(self, matrix):
        # Code here
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]
        self.dp = [[-1 for _ in range(self.n)] for __ in range(self.m)]
        ans = 1

        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(matrix, i, j))

        return ans

        # {
        #  Driver Code Starts
        # Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        ans = obj.longestIncreasingPath(matrix)
        print(ans)

# } Driver Code Ends
