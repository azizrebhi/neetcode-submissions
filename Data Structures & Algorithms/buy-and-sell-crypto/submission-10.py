class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        r=0
        for l in range(1,len(prices)):
            if prices[l]<prices[r]:
                r=l
            else :
               profit=max(prices[l]-prices[r],profit)
        return profit