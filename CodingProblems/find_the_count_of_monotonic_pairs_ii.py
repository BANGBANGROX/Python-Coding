from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = max(nums)
        dp = [1 for _ in range(max_value + 1)]
        MOD = 10**9 + 7
        answer = 0

        for i in range(1, n):
            initial_val = max(nums[i] - nums[i - 1], 0)
            dp2 = [0 for _ in range(max_value + 1)]
            for val in range(initial_val, nums[i] + 1):
                dp2[val] = (
                    dp[val - initial_val] + (dp2[val - 1] if val > 0 else 0)
                ) % MOD
            dp = dp2

        for i in range(0, nums[n - 1] + 1):
            answer = (answer + dp[i]) % MOD

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = []

        for _ in range(n):
            nums.append(int(input()))

        print(Solution().countOfPairs(nums=nums))
