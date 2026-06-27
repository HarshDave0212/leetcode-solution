class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0 
        l = 0
        r = 1
        while r < len(prices):
            maxProf = max(maxProf, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r+=1
        return maxProf