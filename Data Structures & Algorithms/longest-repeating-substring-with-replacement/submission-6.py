class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 # sliding window left idx
        hashmap = {} # keep track of chars in window

        maxf = 0 # running max frequency
        for r in range(len(s)):
            # update hashmap
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxf = max(maxf, hashmap[s[r]])

            # if we have allowed more chars than replacement
            # window is already at its max length
            if r - l + 1 - maxf > k:
                hashmap[s[l]] -= 1
                l += 1
    
        return r - l + 1