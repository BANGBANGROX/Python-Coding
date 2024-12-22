import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        q: int = len(queries)
        n: int = len(heights)
        answer: list[int] = [-1] * q
        pq: list[list[int]] = []
        remaining_queries: list[list[list[int]]] = [[] for _ in range(n)]

        for i in range(q):
            alice_idx = queries[i][0]
            bob_idx = queries[i][1]
            if alice_idx > bob_idx and heights[alice_idx] > heights[bob_idx]:
                answer[i] = alice_idx
            elif alice_idx < bob_idx and heights[alice_idx] < heights[bob_idx]:
                answer[i] = bob_idx
            elif alice_idx == bob_idx:
                answer[i] = alice_idx
            else:
                remaining_queries[max(alice_idx, bob_idx)].append(
                    [max(heights[alice_idx], heights[bob_idx]), i])

        for i in range(n):
            while len(pq) > 0 and pq[0][0] < heights[i]:
                answer[heapq.heappop(pq)[1]] = i
            for query in remaining_queries[i]:
                heapq.heappush(pq, query)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        heights: list[int] = [int(input()) for _ in range(n)]
        q: int = int(input())
        queries: list[list[int]] = [[int(input()), int(input())] for _ in range(q)]

        print(Solution().leftmostBuildingQueries(heights, queries))