from functools import cmp_to_key
from typing import List


class Pair:
    def __init__(self, first: int, second: int) -> None:
        self.first = first
        self.second = second


class Solution:
    def __init__(self) -> None:
        self._grid: list[list[Pair]] = None
        self._dp: list[list[int]] = None
        self._first_rook_position = 0
        self._INF = 10**16

    def _maximum_value_sum_handler(self, row: int, second_rook_position: int) -> int:
        if row >= len(self._grid):
            return -1 * self._INF

        if self._dp[row][second_rook_position + 1] != -1:
            return self._dp[row][second_rook_position + 1]

        result = self._maximum_value_sum_handler(
            row=row + 1, second_rook_position=second_rook_position
        )

        for col in range(3):
            if (
                self._grid[row][col].second != self._first_rook_position
                and self._grid[row][col].second != second_rook_position
            ):
                if second_rook_position == -1:
                    result = max(
                        result,
                        self._grid[row][col].first
                        + self._maximum_value_sum_handler(
                            row=row + 1, second_rook_position=self._grid[row][col].second
                        ),
                    )
                else:
                    result = max(result, self._grid[row][col].first)

        self._dp[row][second_rook_position + 1] = result

        return result

    def _compare(self, a: list[Pair], b: list[Pair]) -> int:
        for i in range(len(a)):
            if a[i].first != b[i].first:
                return b[i].first - a[i].first

        return 1

    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        self._grid = [[None for _ in range(n)] for _ in range(m)]
        answer = -1 * self._INF

        for i in range(m):
            for j in range(n):
                self._grid[i][j] = Pair(board[i][j], j)
            self._grid[i].sort(key=lambda x: -1 * x.first)

        self._grid = sorted(self._grid, key=cmp_to_key(self._compare))

        for col in range(3):
            self._first_rook_position = self._grid[0][col].second
            self._dp = [[-1 for _ in range(n + 1)] for _ in range(m)]
            answer = max(
                answer,
                self._grid[0][col].first
                + self._maximum_value_sum_handler(row=1, second_rook_position=-1),
            )

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        m = int(input())
        n = int(input())
        board = List()

        for _ in range(m):
            current_board = List()
            for _ in range(n):
                current_board.append(int(input()))
            board.append(current_board)
            
        print(Solution().maximumValueSum(board=board))
        