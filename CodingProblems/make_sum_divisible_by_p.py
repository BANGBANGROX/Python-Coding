class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total_sum: int = sum(nums)

        if total_sum % p == 0:
            return 0

        running_sum = 0
        required_rem = total_sum % p
        rem_last_index: dict[int, int] = {0: -1}
        n = len(nums)
        answer = n

        for i in range(n):
            running_sum += nums[i]
            running_sum %= p
            prev_rem = (p + running_sum - required_rem) % p
            if prev_rem in rem_last_index:
                answer = min(answer, i - rem_last_index[prev_rem])
            rem_last_index[running_sum] = i

        return answer if answer < n else -1


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())
        p: int = int(input())

        print(Solution().minSubarray(nums=nums, p=p))
