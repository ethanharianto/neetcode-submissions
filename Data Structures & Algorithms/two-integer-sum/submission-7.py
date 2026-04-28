class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashdict = {}
        for i, num in enumerate(nums):
            if target - num in hashdict:
                return [hashdict[target-num], i]
            hashdict[num] = i