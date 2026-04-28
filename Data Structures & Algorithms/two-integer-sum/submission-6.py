class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add = {}

        for i, num in enumerate(nums):
            if (target - num) in add:
                return [add[target - num], i]
            add[num] = i

        return 