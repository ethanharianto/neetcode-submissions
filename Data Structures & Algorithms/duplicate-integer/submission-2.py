class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            stash = set()
            for num in nums:
                if num in stash:
                    return True
                else:
                    stash.add(num)
            return False