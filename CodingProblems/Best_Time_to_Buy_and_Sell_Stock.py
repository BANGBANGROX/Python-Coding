from ast import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0;
        minPrice = prices[0];
        n = len(prices);
        
        for i in range(1, n) :
            if prices[i] > minPrice :
                maxProfit = max(maxProfit, prices[i] - minPrice);
            else :
                minPrice = prices[i];

        return maxProfit;            

        