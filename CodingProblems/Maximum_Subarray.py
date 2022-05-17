class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums);
        currentSum = 0;
        maxSum = -1 * int(1e9 + 5);

        for num in nums :
            currentSum = max(num, currentSum + num);
            maxSum = max(maxSum, currentSum);
        
        return maxSum;