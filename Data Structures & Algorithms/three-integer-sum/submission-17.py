class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(len(nums) - 2):
            a = nums[i]
            if a > 0:
                break

            target = -a
            j = i + 1
            k = len(nums) - 1
            while j < k:
                num = nums[j] + nums[k]
                if num == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif num < target:
                    j += 1
                else:
                    k -= 1


        return list(res)