class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate through a set and check if the num has been seen already
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False