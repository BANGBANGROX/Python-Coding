class NumMatrix(object):

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[i][j] += matrix[i][j - 1]
                elif j == 0:
                    matrix[i][j] += matrix[i - 1][j]
                else:
                    matrix[i][j] += (matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1])

        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        val1 = self.matrix[row2][col2]
        val2 = 0
        val3 = 0
        val4 = 0

        if row1 > 0:
            val2 = self.matrix[row1 - 1][col2]

        if col1 > 0:
            val3 = self.matrix[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            val4 = self.matrix[row1 - 1][col1 - 1]

        return val1 - val2 - val3 + val4
