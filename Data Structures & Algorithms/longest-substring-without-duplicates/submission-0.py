class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of the characters in substring
        charset = set()

        # keep track of starting letter
        l = 0

        res = 0

        for r in range(len(s)):
            # because we cannot have duplicates, we need to remove s[r]
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res
