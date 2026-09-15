class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):

            if num > 0:
                break

            # dont forget
            if i > 0 and num == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = 0 - num
            while j < k:
                added = nums[j] + nums[k]
                if added < target:
                    j += 1
                elif added > target:
                    k -= 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1
                    # dont forget
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res