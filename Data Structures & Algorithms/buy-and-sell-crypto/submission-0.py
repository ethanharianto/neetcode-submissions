class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minSoFar = prices[0]

        for price in prices:
            minSoFar = min(price, minSoFar)
            res = max(res, price - minSoFar)
        
        return res
