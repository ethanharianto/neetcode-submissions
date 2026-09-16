class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict_s1 = {}

        for ch in s1:
            dict_s1[ch] = dict_s1.get(ch, 0) + 1
        
        dict_s2 = {}

        l = 0
        for r in range(len(s1)):
            dict_s2[s2[r]] = dict_s2.get(s2[r], 0) + 1


        for r in range(len(s1), len(s2)):
            if dict_s2 == dict_s1:
                return True
            dict_s2[s2[r]] = dict_s2.get(s2[r], 0) + 1
            dict_s2[s2[l]] -= 1
            if dict_s2[s2[l]] == 0:
                del dict_s2[s2[l]]
            l += 1
        return dict_s2 == dict_s1
