class Solution:
    def __init__(self):
        self.__tree: list[list[int]] | None = None
        self.__values: list[int] | None = None
        self.__k: int = 0
        self.__answer: int = 0

    def __dfs(self, node: int, parent: int) -> int:
        current_sum = self.__values[node] % self.__k

        for child in self.__tree[node]:
            if child != parent:
                current_sum = (current_sum + self.__dfs(child, node)) % self.__k

        if current_sum == 0:
            self.__answer += 1

        return current_sum

    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int],
                                k: int) -> int:
        self.__tree = [[] for _ in range(n)]
        self.__values = values
        self.__k = k
        self.__answer = 0

        for edge in edges:
            self.__tree[edge[0]].append(edge[1])
            self.__tree[edge[1]].append(edge[0])

        self.__dfs(0, -1)

        return self.__answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        edges: list[list[int]] = [[int(input()), int(input())] for _ in range(n - 1)]
        values: list[int] = [int(input()) for _ in range(n)]
        k: int = int(input())

        print(Solution().maxKDivisibleComponents(n, edges, values, k))
