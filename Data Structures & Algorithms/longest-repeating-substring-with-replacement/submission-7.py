class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        maxf = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxf = max(maxf, hashmap[s[r]])
            if r - l + 1 - maxf > k:
                hashmap[s[l]] -= 1
                l += 1
        
        return r - l + 1