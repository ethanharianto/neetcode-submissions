class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addends = {}
        for i, num in enumerate(nums):
            addend = (target - num)
            if addend in addends:
                return [addends[addend], i]
            addends[num] = i
        return 