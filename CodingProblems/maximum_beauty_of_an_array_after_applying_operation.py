class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        n: int = len(nums)
        left: int = 0
        answer: int = 1

        nums.sort()

        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            answer = max(answer, right - left + 1)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [int(input()) for _ in range(n)]
        k: int = int(input())

        print(Solution().maximumBeauty(nums, k))