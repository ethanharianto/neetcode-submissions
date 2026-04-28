class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = float('inf')
        res = 0
        for sell in prices:
            if sell < min_so_far:
                min_so_far = sell
            res = max(res, sell - min_so_far)
        return res
