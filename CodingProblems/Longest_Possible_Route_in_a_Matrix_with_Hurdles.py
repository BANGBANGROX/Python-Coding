

from typing import List


class Solution:
    def longestPathUtil(self, matrix, x, y, targetX, targetY, length):
        m = len(matrix)
        n = len(matrix[0])

        if (x < 0 or y < 0 or x >= m or y >= n or matrix[x][y] == 0):
            return

        if x == targetX and y == targetY:
            self.ans = max(self.ans, length)

        matrix[x][y] = 0

        self.longestPathUtil(matrix, x+1, y, targetX, targetY, length+1)
        self.longestPathUtil(matrix, x, y-1, targetX, targetY, length+1)
        self.longestPathUtil(matrix, x-1, y, targetX, targetY, length+1)
        self.longestPathUtil(matrix, x, y+1, targetX, targetY, length+1)

        matrix[x][y] = 1

    def longestPath(self, mat: List[List[int]], n: int, m: int, xs: int, ys: int, xd: int, yd: int) -> int:
        # code here
        self.ans = -1

        self.longestPathUtil(mat, xs, ys, xd, yd, 0)

        return self.ans


# {
#  Driver Code Starts


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        a = IntArray().Input(2)

        b = IntArray().Input(4)

        mat = IntMatrix().Input(a[0], a[0])

        obj = Solution()
        res = obj.longestPath(mat, a[0], a[1], b[0], b[1], b[2], b[3])

        print(res)


# } Driver Code Ends
