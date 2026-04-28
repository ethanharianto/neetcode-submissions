class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        cur = set()
        res = 0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])
            res = max(res, r - l + 1)
        return res

