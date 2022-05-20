from typing import List


class Solution:
    def binarySearch(self, nums: List[int], key: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + ((r - l) >> 1))
            if nums[mid] == key:
                return True
            elif nums[mid] > key:
                r = mid - 1
            else:
                l = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0, m):
            if target < matrix[i][0]:
                return False
            if target > matrix[i][n - 1]:
                continue
            return self.binarySearch(matrix[i], target)

        return False
