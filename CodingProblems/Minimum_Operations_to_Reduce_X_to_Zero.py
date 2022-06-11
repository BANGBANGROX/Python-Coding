from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        index = {}
        ans = int(1e9)

        prefix[0] = nums[0]
        suffix[n - 1] = nums[n - 1]
        index[suffix[n - 1]] = n - 1

        if x == suffix[n - 1]:
            return 1

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
            if x == suffix[i]:
                ans = min(ans, n - i)
            index[suffix[i]] = i

        for i in range(n):
            if x < prefix[i]:
                break
            if x == prefix[i]:
                ans = min(ans, i + 1)
            if index.get(x - prefix[i]) != None:
                j = index[x - prefix[i]]
                if i < j:
                    ans = min(ans, n - j + i + 1)

        if ans == int(1e9):
            ans = -1

        return ans
