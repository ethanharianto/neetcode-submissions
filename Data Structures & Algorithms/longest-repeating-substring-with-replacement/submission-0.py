class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # did not keep track of maxf correctly
        res = 0

        l = 0

        seen = {}
        maxf = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxf = max(seen[s[r]], maxf)

            while r - l + 1 > maxf + k:
                seen[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res 



            