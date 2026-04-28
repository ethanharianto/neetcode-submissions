class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        i = 0
        j = 0
        res = 0
        while j < len(s):
            while s[j] in hash:
                hash.remove(s[i])
                i += 1
            else:
                hash.add(s[j])
                res = max(res, j - i + 1)
            j += 1
        return res
