import heapq


class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        m: int = len(grid)
        n: int = len(grid[0])
        pq: list[list[int]] = []
        INF: int = 10**9
        distance: list[list[int]] = [[INF for _ in range(n)] for _ in range(m)]
        directions: list[list[int]] = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        distance[0][0] = 0
        heapq.heappush(pq, [distance[0][0], 0, 0])

        while len(pq) > 0:
            current: list[int] = heapq.heappop(pq)
            current_distance: int = current[0]
            x: int = current[1]
            y: int = current[2]
            if current_distance > distance[x][y]:
                continue
            for direction in directions:
                new_x: int = x + direction[0]
                new_y: int = y + direction[1]
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    new_distance: int = current_distance + grid[new_x][new_y]
                    if new_x == m - 1 and new_y == n - 1:
                        return new_distance
                    if new_distance < distance[new_x][new_y]:
                        distance[new_x][new_y] = new_distance
                        heapq.heappush(pq, [distance[new_x][new_y], new_x, new_y])

        return distance[m - 1][n - 1]


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        m: int = int(input())
        n: int = int(input())
        grid: list[list[int]] = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = int(input())

        print(Solution().minimumObstacles(grid=grid))
