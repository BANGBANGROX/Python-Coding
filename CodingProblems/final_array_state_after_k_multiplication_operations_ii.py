from typing import List
import heapq


class Solution:
    def __init__(self) -> None:
        self.__MOD = 10**9 + 7

    def __binary_exponentiation(self, a: int, b: int) -> int:
        result = 1

        while b > 0:
            if (b & 1) > 0:
                result = (result * a) % self.__MOD
                b -= 1
            a = (a * a) % self.__MOD
            b //= 1

        return result

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums

        min_heap = []
        n = len(nums)
        max_value = max(nums)
        answer = [0] * n

        for i in range(n):
            min_heap.append([nums[i], i])

        heapq.heapify(min_heap)

        while k > 0 and len(min_heap) > 0 and min_heap[0][0] * multiplier <= max_value:
            top_element: list[int] = heapq.heappop(min_heap)
            top_element[0] *= multiplier
            heapq.heappush(min_heap, top_element)
            k -= 1

        if k == 0:
            while len(min_heap) > 0:
                top_element = heapq.heappop(min_heap)
                answer[top_element[1]] = top_element[0] % self.__MOD

            return answer

        extra_operations = k - (k // n * n)

        while extra_operations > 0:
            top_element: list[int] = heapq.heappop(min_heap)
            top_element[0] *= multiplier
            heapq.heappush(min_heap, top_element)
            extra_operations -= 1

        remaining_operations_per_element = (k - extra_operations) // n

        while len(min_heap) > 0:
            top_element: list[int] = heapq.heappop(min_heap)
            idx = top_element[1]
            val = (
                top_element[0]
                * self.__binary_exponentiation(
                    a=multiplier, b=remaining_operations_per_element
                )
            ) % self.__MOD
            answer[idx] = val

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = List[int]()
        for _ in range(n):
            nums.append(int(input()))
        k = int(input())
        multiplier = int(input())

        print(Solution().getFinalState(nums=nums, k=k, multiplier=multiplier))
