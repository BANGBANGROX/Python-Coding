import heapq


class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        pq: list[list[int]] = []
        m: int = len(grid)
        n: int = len(grid[0])
        visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(m)]
        directions: list[list[int]] = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        heapq.heappush(pq, [0, 0, 0])

        while len(pq) > 0:
            current: list[int] = heapq.heappop(pq)
            current_time: int = current[0]
            x: int = current[1]
            y: int = current[2]
            if x == m - 1 and y == n - 1:
                return current_time
            if visited[x][y]:
                continue
            visited[x][y] = True
            for [dx, dy] in directions:
                new_x: int = x + dx
                new_y: int = y + dy
                if (
                    new_x >= 0
                    and new_x < m
                    and new_y >= 0
                    and new_y < n
                    and not visited[new_x][new_y]
                ):
                    wait_time: int = (
                        1 if ((grid[new_x][new_y] - current_time) % 2 == 0) else 0
                    )
                    heapq.heappush(
                        pq,
                        [
                            max(grid[new_x][new_y] + wait_time, current_time + 1),
                            new_x,
                            new_y,
                        ],
                    )

        return -1


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        m: int = int(input())
        n: int = int(input())
        grid: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = int(input())

        print(Solution().minimumTime(grid=grid))
