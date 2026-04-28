class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            # because any number can be used an unlimited amount of times,
            # if taken, we do not increment
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res
