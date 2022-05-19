from ast import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        ans = [[0] * c for i in range(0, r)]

        row = 0
        col = 0

        for i in range(0, m):
            for j in range(0, n):
                ans[row][col] = mat[i][j]
                col += 1
                if (col == c):
                    col = 0
                    row += 1

        return ans
