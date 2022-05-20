from ast import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        stop = False

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Initialize last row
        for i in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][i] == 1:
                stop = True
            if stop:
                obstacleGrid[m - 1][i] = 0
            else:
                obstacleGrid[m - 1][i] = 1

        stop = False

        # Initialize last col
        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 1:
                stop = True
            if stop:
                obstacleGrid[i][n - 1] = 0
            else:
                obstacleGrid[i][n - 1] = 1

        # Fill the rest
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                obstacleGrid[i][j] = obstacleGrid[i + 1][j] + \
                    obstacleGrid[i][j + 1]

        return obstacleGrid[0][0]
