class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_stash = {}
        t_stash = {}
        for i in range(len(s)):
            s_stash[s[i]] = s_stash.get(s[i], 0) + 1
            t_stash[t[i]] = t_stash.get(t[i], 0) + 1
        return s_stash == t_stash
