class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        length = len(res)
        for s in strs[1:]:
            while res != s[:length]:
                length -= 1
                res = res[:length]
        return res
