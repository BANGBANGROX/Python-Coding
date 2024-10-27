class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        answer = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    matrix[i][j] += min(
                        matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]
                    )

        for row in matrix:
            answer += sum(row)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        m: int = int(input())
        n: int = int(input())
        matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(input())

        print(Solution().countSquares(matrix=matrix))
