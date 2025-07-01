class Solution:
    def __init__(self):
        self.__tree: list[list[int]] = []
        self.__cost: list[int] = []
        self.__answer: int = 0

    def min_increase(self, n: int, edges: list[list[int]], cost: list[int]) -> int:
        self.__tree = [[] for _ in range(n)]
        self.__cost = cost
        self.__answer = 0

        for u, v in edges:
            self.__tree[u].append(v)
            self.__tree[v].append(u)

        self.__dfs(0, -1)

        return self.__answer


    def __dfs(self, node: int, parent: int) -> int:
        current_cost: int = self.__cost[node]
        child_costs: list[int] = []

        for child in self.__tree[node]:
            if child != parent:
                child_costs.append(self.__dfs(child, node))

        if not child_costs:
            return current_cost

        max_value: int = max(child_costs)

        for child_cost in child_costs:
            if child_cost != max_value:
                self.__answer += 1

        return current_cost + max_value

if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        edges: list[list[int]] = []
        for _ in range(n - 1):
            edges.append([int(input()), int(input())])
        cost: list[int] = []
        for _ in range(n):
            cost.append(int(input()))

        print(Solution().min_increase(n, edges, cost))

