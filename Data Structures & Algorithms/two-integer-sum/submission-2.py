class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in stack:
                return [stack[diff], i]
            else:
                stack[num] = i
        return