class Solution:
    def findMin(self, nums: list[int]) -> int:
        left: int = 0
        right: int = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid: int = left + ((right - left) >> 1)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[right]


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums[i] = int(input())

        print(Solution().findMin(nums=nums))
