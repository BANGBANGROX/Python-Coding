from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        currentSum = 0

        for i in range(0, n):
            currentSum += nums[i]
            currentSum %= k
            if currentSum == 0 and i > 0:
                return True
            if mp.get(currentSum) is not None:
                length = i - mp[currentSum]
                if length > 1:
                    return True
            else:
                mp[currentSum] = i

        return False


if __name__ == '__main__':
    T = int(input())
    for i in range(0, T):
        n = int(input())
        nums = []
        for i in range(n):
            x = int(input())
            nums.append(x)
        k = int(input())

        solution = Solution()
        print(solution.checkSubarraySum(nums, k))
