class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = set() # keep track of nums seen
        for num in nums:
            if num in stack: # value has appeared already
                return True
            stack.add(num)
        return False # no duplicates
