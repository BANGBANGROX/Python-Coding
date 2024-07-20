from collections import defaultdict
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        prefix_sum = [0] * (k + 1)
        answer = 10**9
        running_sum = 0

        for i in range(n // 2):
            current_diff = abs(nums[i] - nums[n - i - 1])
            max_possible_diff = max(
                max(nums[i], nums[n - i - 1]), max(k - nums[i], k - nums[n - i - 1])
            )
            min_possible_diff = 0
            count[current_diff] += 1
            prefix_sum[min_possible_diff] += 1
            if max_possible_diff + 1 <= k:
                prefix_sum[max_possible_diff + 1] += 1

        for i in range(k + 1):
            running_sum += prefix_sum[i]
            answer = min(answer, running_sum - count.get(i, 0))

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = [0] * n
        for i in range(n):
            nums[i] = int(input())
        k = int(input())

        print(Solution().minChanges(nums=nums, k=k))
