class Solution:
    def max_stability(self, n: int, edges: list[list[int]], k: int) -> int:
        class DisjointSetUnion:
            def __init__(self, n: int) -> None:
                self.__parent: list[int] = [-1] * n
                self.__rank: list[int] = [0] * n

            def find(self, node: int) -> int:
                if self.__parent[node] == -1:
                    return node

                self.__parent[node] = self.find(self.__parent[node])

                return self.__parent[node]

            def union(self, u: int, v: int) -> bool:
                u_par: int = self.find(u)
                v_par: int = self.find(v)

                if u_par == v_par:
                    return False

                if self.__rank[u_par] > self.__rank[v_par]:
                    self.__parent[v_par] = u_par
                else:
                    self.__parent[u_par] = v_par
                    if self.__rank[u_par] == self.__rank[v_par]:
                        self.__rank[v_par] += 1

                return True

        def check(stability: int) -> bool:
            edges_taken: int = 0
            disjoint_set_union: DisjointSetUnion = DisjointSetUnion(n)
            candidate_edges: list[list[int]] = []
            total_cost: int = 0

            for u, v, wt, must in edges:
                if must == 1:
                    if wt < stability or not disjoint_set_union.union(u, v):
                        return False
                    else:
                        edges_taken += 1

            for u, v, wt, must in edges:
                if must == 0:
                    if wt >= stability:
                        candidate_edges.append([0, u, v])
                    elif wt * 2 >= stability:
                        candidate_edges.append([1, u, v])

            candidate_edges.sort()

            for cost, u, v in candidate_edges:
                if total_cost + cost <= k and disjoint_set_union.union(u, v):
                    edges_taken += 1
                    total_cost += cost
                    if edges_taken == n - 1:
                        return True

            return edges_taken == n - 1

        left: int = 0
        right: int = 2 * (10 ** 5)
        answer: int = -1

        while left <= right:
            mid: int = (left + ((right - left) >> 1))
            if check(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        m: int = int(input())
        edges: list[list[int]] = []
        for i in range(m):
            edges.append([int(input()) for _ in range(4)])
        k: int = int(input())
        
        print(Solution().max_stability(n, edges, k))
