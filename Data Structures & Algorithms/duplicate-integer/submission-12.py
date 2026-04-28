class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through nums once, keeping track of seen numbers
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False