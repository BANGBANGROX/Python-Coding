from typing import List


class Solution:
    def lowerBound(self, nums, key):
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid][0] < key:
                l = mid + 1
            else:
                r = mid - 1

        return l

    def maximum_profit(self, n: int, intervals: List[List[int]]) -> int:
        # code here
        dp = [0 for _ in range(n)]

        intervals.sort()

        for i in range(n - 1, -1, -1):
            dp[i] = intervals[i][2]
            idx = self.lowerBound(intervals, intervals[i][1])
            if idx < n:
                dp[i] += dp[idx]
            if i < n - 1:
                dp[i] = max(dp[i], dp[i + 1])

        return dp[0]

        # {
     # Driver Code Starts


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        intervals = IntMatrix().Input(n, 3)

        obj = Solution()
        res = obj.maximum_profit(n, intervals)

        print(res)


# } Driver Code Ends
