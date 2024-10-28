from math import sqrt


class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums.sort()

        length: list[int] = [0] * (nums[-1] + 1)
        answer: int = 0

        for num in nums:
            num_sqrt: float = sqrt(num)
            if num_sqrt == int(num_sqrt):
                length[num] = length[num_sqrt] + 1
            else:
                length[num] = 1
            answer = max(answer, length[num])

        return -1 if answer == 1 else answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())

        print(Solution().longestSquareStreak(nums=nums))
