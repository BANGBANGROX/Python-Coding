class Solution:
    def findMaximumScore(self, nums: list[int]) -> int:
        running_max: int = 0
        answer: int = 0

        for num in nums:
            answer += running_max
            running_max = max(running_max, num)

        return answer


if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())

        print(Solution().findMaximumScore(nums=nums))
