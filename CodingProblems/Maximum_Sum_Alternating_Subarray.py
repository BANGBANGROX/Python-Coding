class Solution:
    def maximumSumAlternatingSubarray(self, nums):
        n = len(nums)
        currentSum = 0
        ans = -1 * int(1e9 + 5)

        for i in range(0, n):
            if (i & 1) > 0:
                currentSum -= nums[i]
            else:
                currentSum = max(currentSum + nums[i], nums[i])
            ans = max(ans, currentSum)

        for i in range(1, n):
            if (i & 1) == 0:
                currentSum -= nums[i]
            else:
                currentSum = max(currentSum + nums[i], nums[i])
            ans = max(ans, currentSum)

        return ans


n = int(input())
nums = [-1] * n
for i in range(0, n):
    nums[i] = int(input())

solution = Solution()
print(solution.maximumSumAlternatingSubarray(nums))
