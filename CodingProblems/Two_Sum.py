from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums);
        indexedNums = [(0, 0)] * n;
    
        for i in range(0, n) :
            indexedNums[i] = (nums[i], i);

        indexedNums.sort();

        l = 0;
        r = n - 1;

        while l < r :
            num1, index1 = indexedNums[l];
            num2, index2 = indexedNums[r];
            if num1 + num2 == target :
                return [index1, index2];
            elif num1 + num2 < target :
                l += 1;
            else :
                r -= 1;

        return [];                    


