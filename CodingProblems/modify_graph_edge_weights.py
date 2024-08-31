from typing import List
import heapq

INF = 10**12


class Solution:
    def __init__(self) -> None:
        self.__edges: list[list[int]] = None
        self.__distance: list[list[int]] = None
        self.__graph: list[list[list[int]]] = None
        self.__source: int = 0

    def __compute_distance(self, difference: int, run: int) -> None:
        min_heap: list[list[int]] = []

        heapq.heappush(min_heap, [0, self.__source])
        self.__distance[self.__source][run] = 0

        while len(min_heap) > 0:
            current: list[int] = heapq.heappop(min_heap)
            current_node: int = current[1]
            current_distance: int = current[0]
            if current_distance > self.__distance[current_node][run]:
                continue
            for child in self.__graph[current_node]:
                next_node: int = child[0]
                edge_index: int = child[1]
                weight: int = self.__edges[edge_index][2]
                if weight == -1:
                    weight = 1
                if run == 1 and self.__edges[edge_index][2] == -1:
                    new_weight: int = (
                        difference
                        + self.__distance[next_node][0]
                        - self.__distance[current_node][1]
                    )
                    if new_weight > weight:
                        self.__edges[edge_index][2] = weight = new_weight
                if (
                    self.__distance[next_node][run]
                    > self.__distance[current_node][run] + weight
                ):
                    self.__distance[next_node][run] = (
                        self.__distance[current_node][run] + weight
                    )
                    heapq.heappush(
                        min_heap, [self.__distance[next_node][run], next_node]
                    )

    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        self.__edges = edges
        self.__distance = [[INF for _ in range(2)] for _ in range(n)]
        self.__graph = [[] for _ in range(n)]
        self.__source = source

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            self.__graph[u].append([v, i])
            self.__graph[v].append([u, i])

        self.__compute_distance(difference=0, run=0)

        difference = target - self.__distance[destination][0]

        if difference < 0:
            return []

        self.__compute_distance(difference=difference, run=1)

        if target != self.__distance[destination][1]:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1

        return edges


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        edge_cnt: int = int(input())
        edges: list[list[int]] = []
        for _ in range(edge_cnt):
            edges.append([int(input()), int(input()), int(input())])
        source: int = int(input())
        destination: int = int(input())
        target: int = int(input())

        print(
            Solution().modifiedGraphEdges(
                n=n, edges=edges, source=source, destination=destination, target=target
            )
        )
