class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        n: int = len(nums)
        left: int = 0
        min_value: int = nums[0] - 2
        max_value: int = nums[0] + 2
        answer: int = 1

        for right in range(1, n):
            if min_value <= nums[right] <= max_value:
                min_value = max(min_value, nums[right] - 2)
                max_value = min(max_value, nums[right] + 2)
            else:
                left = right - 1
                min_value = nums[right] - 2
                max_value = nums[right] + 2
                while min_value <= nums[left] <= max_value:
                    min_value = max(min_value, nums[left] - 2)
                    max_value = min(max_value, nums[left] + 2)
                    left -= 1
                left += 1
            answer += (right - left + 1)

        return answer


if __name__ == "__main__":
    test_cases: int = int(input())
    
    for _ in range(test_cases):
        n: int = int(input())
        nums: list[int] = [0] * n
        for i in range(n):
            nums.append(int(input()))

        print(Solution().continuousSubarrays(nums))