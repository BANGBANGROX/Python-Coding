from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wage_to_quality_ratio = []
        n = len(quality)

        for i in range(n):
            wage_to_quality_ratio.append({
                "ratio": wage[i] / quality[i],
                "index": i,
            })

        wage_to_quality_ratio.sort(key=lambda x: x["ratio"])

        max_ratio = 0
        quality_sum = 0
        max_heap = []

        heapq.heapify(max_heap)

        for i in range(k):
            idx = wage_to_quality_ratio[i]["index"]
            quality_sum += quality[idx]
            max_ratio = max(max_ratio, wage_to_quality_ratio[i]["ratio"])
            heapq.heappush(max_heap, -1 * quality[idx])

        answer = quality_sum * max_ratio

        for i in range(k, n):
            quality_sum -= -1 * heapq.heappop(max_heap)
            idx = wage_to_quality_ratio[i]["index"]
            quality_sum += quality[idx]
            max_ratio = max(max_ratio, wage_to_quality_ratio[i]["ratio"])
            heapq.heappush(max_heap, -1 * quality[idx])
            answer = min(answer, max_ratio * quality_sum)

        return answer


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        quality = []
        wage = []
        for _ in range(n):
            quality.append(int(input()))
        for _ in range(n):
            wage.append(int(input()))
        k = int(input())

        print(Solution().mincostToHireWorkers(quality, wage, k))
