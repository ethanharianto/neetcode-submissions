class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        i = 0
        prefix = []
        curr = 0
        for i in height:
            curr = max(i, curr)
            prefix.append(curr)
        
        suffix = []
        curr = 0
        for i in height[::-1]:
            curr = max(i, curr)
            suffix.append(curr)
        
        for i in range(len(height)):
            res += min(suffix[len(height) - i - 1], prefix[i]) - height[i]
        
        return res