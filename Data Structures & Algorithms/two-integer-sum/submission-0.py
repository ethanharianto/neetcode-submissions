class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stash = {}
        for i in range(len(nums)):
            if (target - nums[i]) in stash:
                return [stash[target - nums[i]], i]
            else:
                stash[nums[i]] = i