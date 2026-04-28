class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we can model this as a growing rectangle and if the rectangle cannot grow further,
        # we calculate it; otherwise, we extend it

        stack = [] # (index, height)

        res = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                idx, h = stack.pop()
                res = max(res, h * (i - idx))
                start = idx
            stack.append((start, height))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        
        return res