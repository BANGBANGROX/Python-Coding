from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        answer = 0
        previous_diff = 0
        sign = 0

        for num, expected_num in zip(nums, target):
            current_diff = expected_num - num
            if sign * current_diff < 0:
                previous_diff = 0
            sign = current_diff
            current_diff = abs(current_diff)
            answer += max(current_diff - previous_diff, 0)
            previous_diff = current_diff

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = [0] * n
        for i in range(n):
            nums[i] = int(input())
        target = [0] * n
        for i in range(n):
            target[i] = int(input())

        print(Solution().minimumOperations(nums=nums, target=target))
