class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            stash = {}
            for num in nums:
                if num in stash:
                    return True
                else:
                    stash[num] = ''
            return False