class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix = []
        curr = 0
        for sell in prices[::-1]:
            curr = max(curr, sell)
            suffix.append(curr)
        
        res = 0
        for i in range(len(prices)):
            res = max(res, suffix[len(prices) - i - 1] - prices[i])
        
        return res
