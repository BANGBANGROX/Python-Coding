from typing import List


class Solution:
    def init(self, nums, k):
        self.nums = nums
        self.k = k
        self.n = len(nums)
        self.power = [0 for _ in range(self.n + 1)]
        self.dp1 = [[-1 for _ in range(k + 1)] for __ in range(self.n)]
        self.dp2 = [[-1 for _ in range(k + 1)] for __ in range(self.n)]
        self.MOD = int(1e9 + 7)

        self.power[0] = 1

        for i in range(1, self.n + 1):
            self.power[i] = (self.power[i - 1] * 2) % self.MOD

    def countPartitionsUtil(self, idx, group1Sum, group2Sum):
        if idx >= self.n:
            if group1Sum >= self.k and group2Sum >= self.k:
                return 1
            return 0

        if group1Sum >= self.k and group2Sum >= self.k:
            return self.power[self.n - idx]

        if group1Sum <= self.k and self.dp1[idx][group1Sum] != -1:
            return self.dp1[idx][group1Sum]

        if group2Sum <= self.k and self.dp2[idx][group2Sum] != -1:
            return self.dp2[idx][group2Sum]

        ans = (self.countPartitionsUtil(idx + 1, group1Sum + self.nums[idx], group2Sum) +
               self.countPartitionsUtil(idx + 1, group1Sum, group2Sum + self.nums[idx])) % self.MOD

        if group1Sum <= self.k:
            self.dp1[idx][group1Sum] = ans

        if group2Sum <= self.k:
            self.dp2[idx][group2Sum] = ans

        return ans

    def countPartitions(self, nums: List[int], k: int) -> int:
        self.init(nums, k)

        return self.countPartitionsUtil(0, 0, 0)


if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        n = int(input())
        nums = []
        for j in range(n):
            x = int(input())
            nums.append(x)
        k = int(input())

        solution = Solution()
        print(solution.countPartitions(nums, k))
