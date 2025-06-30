class Solution:
    def min_xor(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        dp: list[list[int]] = [[-1 for _ in range(k + 1)] for _ in range(n)]
        max_value: int = 10 ** 12

        def min_xor_handler(idx: int, parts_left: int) -> int:
            if idx == n and parts_left == 0:
                return 0

            if idx == n or parts_left == 0:
                return max_value

            if dp[idx][parts_left] != -1:
                return dp[idx][parts_left]

            current_xor = 0
            result = max_value

            for i in range(idx, n - parts_left + 1):
                current_xor ^= nums[i]
                next_xor = min_xor_handler(i + 1, parts_left - 1)
                result = min(result, max(current_xor, next_xor))

            dp[idx][parts_left] = result

            return result

        return min_xor_handler(0, k)


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        print(Solution().min_xor(nums=[int(input()) for _ in range(int(input()))], k=int(input())))
