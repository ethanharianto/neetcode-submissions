class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stash = {}
        for num in nums:
            stash[num] = stash.get(num, 0) + 1
        return sorted(stash, key=lambda n: stash[n], reverse=True)[:k]