def _rotate(grid: list[list[int]]) -> list[list[int]]:
    return list(zip(*reversed(grid)))


class Solution:
    class Container:
        def __init__(self):
            INF = 10**9
            self.min_x = self.min_y = INF
            self.max_x = self.max_y = -1 * INF

        def add_point(self, x: int, y: int) -> None:
            self.min_x = min(self.min_x, x)
            self.max_x = max(self.max_x, x)
            self.min_y = min(self.min_y, y)
            self.max_y = max(self.max_y, y)

        def calculate_area(self) -> int:
            return (self.max_x - self.min_x + 1) * (self.max_y - self.min_y + 1)

    def __init_containers(self) -> list[Container]:
        return [self.Container() for _ in range(3)]

    def __solve_2_figure_case(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = m * n

        for i in range(m):
            for j in range(i + 1, m):
                containers = self.__init_containers()
                for x in range(m):
                    for y in range(n):
                        if grid[x][y] == 1:
                            if x <= i:
                                containers[0].add_point(x, y)
                            elif x <= j:
                                containers[1].add_point(x, y)
                            else:
                                containers[2].add_point(x, y)
                result = min(result, containers[0].calculate_area() + containers[1].calculate_area() +
                             containers[2].calculate_area())

        return result

    def __solve_4_figure_case(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = m * n

        for i in range(m):
            for j in range(n):
                containers = self.__init_containers()
                for x in range(m):
                    for y in range(n):
                        if grid[x][y] == 1:
                            if x <= i:
                                containers[0].add_point(x, y)
                            elif y <= j:
                                containers[1].add_point(x, y)
                            else:
                                containers[2].add_point(x, y)
                result = min(result, containers[0].calculate_area() + containers[1].calculate_area() + containers[
                    2].calculate_area())

        return result

    def minimumSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = m * n

        first_rotate = _rotate(grid)
        second_rotate = _rotate(first_rotate)
        third_rotate = _rotate(second_rotate)

        result = min(result, self.__solve_2_figure_case(grid))
        result = min(result, self.__solve_2_figure_case(first_rotate))

        result = min(result, self.__solve_4_figure_case(grid))
        result = min(result, self.__solve_4_figure_case(first_rotate))
        result = min(result, self.__solve_4_figure_case(second_rotate))
        result = min(result, self.__solve_4_figure_case(third_rotate))

        return result

