from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_ind = 0
        last_index = [-1] * n
        dp = [0] * n
        answer = []

        nums.sort()

        dp[0] = 1
        last_index[0] = 0

        for i in range(1, n):
            dp[i] = 1
            last_index[i] = i
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    last_index[i] = j
            if dp[i] > dp[max_ind]:
                max_ind = i

        while last_index[max_ind] != max_ind:
            answer.append(nums[max_ind])
            max_ind = last_index[max_ind]

        answer.append(nums[max_ind])

        return answer
