class Solution:
    def maximumSubarrayXor(
        self, nums: list[int], queries: list[list[int]]
    ) -> list[int]:
        n: int = len(nums)
        dp: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]
        answer: list[int] = []

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j] ^ dp[i][j - 1]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])

        for query in queries:
            answer.append(dp[query[0]][query[1]])

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())
        q: int = int(input())
        queries: list[list[int]] = [[0 for _ in range(2)] for _ in range(q)]
        for i in range(q):
            queries[i][0] = int(input())
            queries[i][1] = int(input())

        print(Solution().maximumSubarrayXor(nums=nums, queries=queries))
