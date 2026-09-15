class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        j = 0
        res = 0
        curr = 0

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
            curr = j - i
            res = max(curr, res)
        return res
        