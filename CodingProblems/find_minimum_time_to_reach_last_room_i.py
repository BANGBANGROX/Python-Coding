import heapq


INF: int = 10**10

class _Cell:
    def __init__(self, x: int, y: int, distance: int):
        self.x = x
        self.y = y
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def min_time_to_reach(self, move_time: list[list[int]]) -> int:
        pq: list[_Cell] = []
        m: int = len(move_time)
        n: int = len(move_time[0])
        distance: list[list[int]] = [[INF for _ in range(n)] for _ in range(m)]
        directions: list[list[int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        distance[0][0] = 0
        heapq.heappush(pq, _Cell(0, 0, distance[0][0]))

        while len(pq) > 0:
            cell: _Cell = heapq.heappop(pq)
            x: int = cell.x
            y: int = cell.y
            curr_distance = cell.distance
            if curr_distance > distance[x][y]:
                continue
            for dir in directions:
                new_x = x + dir[0]
                new_y = y + dir[1]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                    continue
                new_distance = max(curr_distance, move_time[new_x][new_y]) + 1
                if new_distance < distance[new_x][new_y]:
                    heapq.heappush(pq, _Cell(new_x, new_y, new_distance))
                    distance[new_x][new_y] = new_distance

        return distance[m - 1][n - 1]


if __name__ == '__main__':
    test_cases: int = int(input())

    for _ in range(test_cases):
        m: int = int(input())
        n: int = int(input())
        move_time: list[list[int]] = [[int(input()) for _ in range(n)] for _ in range(m)]

        print(Solution().min_time_to_reach(move_time=move_time))