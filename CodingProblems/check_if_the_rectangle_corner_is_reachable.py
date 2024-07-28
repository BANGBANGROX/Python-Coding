from typing import List


class Solution:
    def __init__(self):
        self.__parent: list[int] = []

    def __find(self, node: int) -> int:
        if self.__parent[node] == node:
            return node

        self.__parent[node] = self.__find(self.__parent[node])

        return self.__parent[node]

    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        self.__parent = [_ for _ in range(n + 2)]

        for i in range(n):
            x, y, r = circles[i]
            if x - r <= 0 or y + r >= Y:
                self.__parent[self.__find(node=n)] = self.__find(node=i)
            if x + r >= X or y - r <= 0:
                self.__parent[self.__find(node=n + 1)] = self.__find(node=i)
            for j in range(i + 1, n):
                x1, y1, r1 = circles[j]
                if (x - x1) ** 2 + (y - y1) ** 2 - (r + r1) ** 2 <= 0:
                    self.__parent[self.__find(node=i)] = self.__find(node=j)

        return self.__find(node=n) != self.__find(node=n + 1)


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        X = int(input())
        Y = int(input())
        n = int(input())
        circles = [[0 for _ in range(3)] for _ in range(n)]
        for i in range(n):
            circles[i][0] = int(input())
            circles[i][1] = int(input())
            circles[i][2] = int(input())

        print(Solution().canReachCorner(X=X, Y=Y, circles=circles))
