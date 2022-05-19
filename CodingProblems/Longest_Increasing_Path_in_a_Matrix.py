from ast import List


class Solution:
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    distance = [[]]

    def dfs(self, matrix: List[List[int]], x, y):
        m = len(matrix)
        n = len(matrix[0])
        maxLen = 0

        for i in range(0, 4):
            newX = x + self.dx[i]
            newY = y + self.dy[i]
            if newX >= 0 and newY >= 0 and newX < m and newY < n and matrix[newX][newY] > matrix[x][y]:
                if self.distance[newX][newY] == -1:
                    self.dfs(self, matrix, newX, newY)
                maxLen = max(maxLen, self.distance[newX][newY])

        self.distance[x][y] = 1 + maxLen

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        self.distance = [[-1] * n for i in range(0, m)]
        ans = 1

        for i in range(0, m):
            for j in range(0, n):
                if self.distance[i][j] == -1:
                    self.dfs(matrix, i, j)
                    ans = max(ans, self.distance[i][j])

        return ans
