class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n: int = len(arr)
        left: int = 0
        right: int = n - 1

        while left < right:
            mid: int = left + ((right - left) >> 1)
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    test_cases: int = int(input())

    for _ in range(test_cases):
        n: int = int(input())
        arr: list[int] = [int(input()) for _ in range(n)]

        print(Solution().peakIndexInMountainArray(arr=arr))
