from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0;
        r = n - 1;
        
        while l < r:
            currentSum = numbers[l] + numbers[r];
            if currentSum == target:
                return [l + 1, r + 1];
            elif currentSum > target:
                r -= 1;
            else:
                l += 1;
        
        return [-1, -1];                    