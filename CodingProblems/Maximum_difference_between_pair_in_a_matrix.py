from typing import List


class Solution:
    def findMaxValue(self, n: int, mat: List[List[int]]) -> int:
        # code here
        ans = -1 * int(1e9)

        for i in range(1, n):
            mat[i][0] = min(mat[i][0], mat[i - 1][0])
            mat[0][i] = min(mat[0][i], mat[0][i - 1])

        for i in range(1, n):
            for j in range(1, n):
                ans = max(ans, mat[i][j] - mat[i - 1][j - 1])
                mat[i][j] = min(mat[i][j], min(mat[i][j - 1], mat[i - 1][j]))

        return ans

        # {
     # Driver Code Starts


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

        n = int(input())

        mat = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.findMaxValue(n, mat)

        print(res)


# } Driver Code Ends
