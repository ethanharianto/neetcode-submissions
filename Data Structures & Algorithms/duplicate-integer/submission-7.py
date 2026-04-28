class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = set()
        for num in nums:
            if num in stack:
                return True
            stack.add(num)
        return False