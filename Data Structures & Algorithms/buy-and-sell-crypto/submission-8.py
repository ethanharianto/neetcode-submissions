class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf') # keep track of the minimum buy price
        res = 0

        for price in prices:
            min_so_far = min(min_so_far, price)
            res = max(res, price - min_so_far)
        
        return res