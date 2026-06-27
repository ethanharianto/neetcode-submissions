class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        first = strs[0]
        last = strs[len(strs)-1]
        for i in range(len(first)):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
        return res

            
