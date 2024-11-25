class Solution:
    def __init__(self) -> None:
        self.__string_to_moves: dict[str, int] = None

    def __swap(self, current_str: str, pos1: int, pos2: int) -> str:
        current_str_list: list[str] = list(current_str)
        temp: str = current_str_list[pos1]
        current_str_list[pos1] = current_str_list[pos2]
        current_str_list[pos2] = temp

        return "".join(current_str_list)

    def __dfs(self, current_str: str, current_pos: int, moves: int) -> None:
        if (
            current_str in self.__string_to_moves
            and self.__string_to_moves[current_str] <= moves
        ):
            return

        directions: list[list[int]] = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]
        self.__string_to_moves[current_str] = moves

        for next_pos in directions[current_pos]:
            next_str: str = self.__swap(
                current_str=current_str, pos1=current_pos, pos2=next_pos
            )
            self.__dfs(current_str=next_str, current_pos=next_pos, moves=moves + 1)

    def slidingPuzzle(self, board: list[list[int]]) -> int:
        self.__string_to_moves = {}
        starting_point_list: list[str] = []

        for row in board:
            for val in row:
                starting_point_list.append(str(val))

        starting_point: str = "".join(starting_point_list)

        self.__dfs(
            current_str=starting_point, current_pos=starting_point.find("0"), moves=0
        )

        return self.__string_to_moves.get("123450", -1)


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        board: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]
        for i in range(2):
            for j in range(3):
                board[i][j] = int(input())

        print(Solution().slidingPuzzle(board=board))
