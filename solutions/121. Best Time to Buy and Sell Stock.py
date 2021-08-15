class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP,profit)
            else:
                l = r
            r += 1
        return maxP
        
        
        
        
        
# [7,1,5,3,6,4]
# take first as 1st day
# travers through the list
# find least first and then highest at last
