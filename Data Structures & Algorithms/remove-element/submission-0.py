class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums)
        i = 0
        while i < j:
            if nums[i] == val:
                j -= 1
                nums[i] = nums[j]
            else:
                i += 1
        return j