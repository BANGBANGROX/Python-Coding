from collections import deque, defaultdict


class Solution:
    def __init__(self) -> None:
        self.__graph: dict[int, deque[int]] = None
        self.__nodes_in_path: list[int] = None

    def __dfs(self, node: int) -> None:
        neighbors: deque[int] = self.__graph.get(node)

        while neighbors is not None and len(neighbors) > 0:
            child: int = neighbors.popleft()
            self.__dfs(node=child)

        self.__nodes_in_path.append(node)

    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        self.__graph = {}
        self.__nodes_in_path = []
        in_degree: dict[int, int] = defaultdict(int)
        out_degree: dict[int, int] = defaultdict(int)
        start_node: int = -1
        answer: list[list[int]] = []

        for [start, end] in pairs:
            if start not in self.__graph:
                self.__graph[start] = deque()
            self.__graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        for node, cnt in out_degree.items():
            if cnt == in_degree[node] + 1:
                start_node = node
                break

        if start_node == -1:
            start_node = pairs[0][0]

        self.__dfs(node=start_node)
        self.__nodes_in_path.reverse()

        for i in range(1, len(self.__nodes_in_path)):
            answer.append([self.__nodes_in_path[i - 1], self.__nodes_in_path[i]])

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        pairs: list[list[int]] = [[int(input()) for _ in range(2)] for _ in range(n)]

        print(Solution().validArrangement(pairs=pairs))
