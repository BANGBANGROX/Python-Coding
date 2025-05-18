MOD: int = 10 ** 9 + 7


class Solution:
    def __init__(self):
        self.__dp: list[list[int]] = []
        self.__m: int = 0
        self.__n: int = 0
        self.__FULL_MASK: int = 3

    def color_the_grid(self, m: int, n: int) -> int:
        self.__m = m
        self.__n = n
        self.__dp = [[-1 for _ in range(1025)] for _ in range(n)]

        return self.__color_the_grid_handler(current_row=0, current_col=0, previous_state=0, current_state=0)

    def __color_the_grid_handler(self, current_row: int, current_col: int, previous_state: int,
                                 current_state: int) -> int:
        if current_col == self.__n:
            return 1

        if current_row == self.__m:
            return self.__color_the_grid_handler(current_row=0, current_col=current_col + 1,
                                                 previous_state=current_state, current_state=0)

        if current_row == 0 and self.__dp[current_col][previous_state] != -1:
            return self.__dp[current_col][previous_state]

        upper_color: int = (current_state & self.__FULL_MASK)
        left_color: int = ((previous_state >> ((self.__m - current_row - 1) * 2)) & self.__FULL_MASK)
        total_ways: int = 0

        for color in range(1, 4):
            if color != upper_color and color != left_color:
                total_ways = (total_ways + self.__color_the_grid_handler(current_row=current_row + 1,
                                                                         current_col=current_col,
                                                                         previous_state=previous_state, current_state=(
                                                                                                                              current_state << 2) + color)) % MOD

        if current_row == 0:
            self.__dp[current_col][previous_state] = total_ways

        return total_ways


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().color_the_grid(m=int(input()), n=int(input())))
