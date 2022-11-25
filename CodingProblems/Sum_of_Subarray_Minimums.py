from typing import List


class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        MOD = 1e9 + 7
        ans = 0
        n = len(nums)
        stack = []

        for i in range(n + 1):
            while len(stack) > 0 and (i == n or nums[stack[-1]] >= nums[i]):
                mid = stack.pop()
                left = -1 if len(stack) == 0 else stack[-1]
                count = ((mid - left) * (i - mid)) % MOD
                ans = (ans + (count * nums[mid])) % MOD
            stack.append(i)

        return ans


if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        n = int(input())
        nums = []
        for i in range(n):
            x = int(input())
            nums.append(x)

        solution = Solution()
        print(solution.sumSubarrayMins(nums))
