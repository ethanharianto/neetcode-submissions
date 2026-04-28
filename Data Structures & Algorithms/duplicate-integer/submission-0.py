class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         stack = set()
         for num in nums:
            stack.add(num)
         return not (len(stack) == len(nums))