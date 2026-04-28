class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        frequencies = [[] for i in range(len(nums) + 1)]

        for num in counts:
            frequencies[counts[num]].append(num)
        
        res = []
        for i in range(len(frequencies) - 1, 0, - 1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res