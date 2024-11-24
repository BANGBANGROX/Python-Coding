class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        non_positive_elements: int = 0
        min_value = 10**9
        answer: int = 0

        for row in matrix:
            for val in row:
                if row <= 0:
                    non_positive_elements += 1
                answer += abs(val)
                min_value = min(min_value, abs(val))

        if (non_positive_elements & 1) > 0:
            answer -= 2 * min_value

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = int(input())

        print(Solution().maxMatrixSum(matrix=matrix))
