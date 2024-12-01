class Solution:
    def __init__(self) -> None:
        self.__tree: list[list[int]] = None
        self.__count: list[int] = None
        self.__answer: list[int] = None

    def __dfs(self, node: int, parent: int, level: int) -> None:
        self.__count[level % 2] += 1

        for child in self.__tree[node]:
            if child != parent:
                self.__dfs(child, node, level + 1)

    def __populate_answer(self, node: int, parent: int, level: int) -> None:
        self.__answer[node] += self.__count[level % 2]

        for child in self.__tree[node]:
            if child != parent:
                self.__populate_answer(child, node, level + 1)

    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        m: int = len(edges1) + 1
        n: int = len(edges2) + 1
        tree1: list[list[int]] = [[] for _ in range(m)]
        tree2: list[list[int]] = [[] for _ in range(n)]
        self.__count = [0, 0]

        for [u, v] in edges1:
            tree1[u].append(v)
            tree1[v].append(u)

        for [u, v] in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        self.__tree = tree2

        for i in range(n):
            if len(tree2[i]) == 1:
                self.__dfs(i, -1, 0)
                break

        self.__tree = tree1
        self.__answer = [max(self.__count[0], self.__count[1]) for _ in range(m)]
        self.__count = [0, 0]

        print(self.__answer)

        for i in range(m):
            if len(tree1[i]) == 1:
                self.__dfs(i, -1, 0)
                self.__populate_answer(i, -1, 0)
                break

        return self.__answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        m: int = int(input())
        edges1: list[list[int]] = [[int(input()), int(input())] for _ in range(m - 1)]
        n: int = int(input())
        edges2: list[list[int]] = [[int(input()), int(input())] for _ in range(n - 1)]

        print(Solution().maxTargetNodes(edges1, edges2))
