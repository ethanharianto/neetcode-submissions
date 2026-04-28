class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make dictionaries and compare
        s_dict = {}
        t_dict = {}

        for ch in s:
            s_dict[ch] = s_dict.get(ch,0) + 1

        for ch in t:
            t_dict[ch] = t_dict.get(ch,0) + 1

        return s_dict == t_dict