from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        INF: int = 10**9
        n: int = len(nums)
        dq: deque[int] = deque()
        answer: int = INF
        prefix_sum: list[int] = [0] * n

        for i in range(n):
            prefix_sum[i] = nums[i] + (prefix_sum[i - 1] if i > 0 else 0)

        for i in range(n):
            if prefix_sum[i] >= k:
                answer = min(answer, i + 1)
            while len(dq) > 0 and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                answer = min(answer, i - dq.popleft())
            while len(dq) > 0 and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)

        return answer if answer != INF else -1


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())
        k: int = int(input())

        print(Solution().shortestSubarray(nums=nums, k=k))
