class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash, s2_hash = {}, {}
        for i in range(len(s1)):
            s1_hash[s1[i]] = s1_hash.get(s1[i], 0) + 1
            s2_hash[s2[i]] = s2_hash.get(s2[i], 0) + 1
        
        matches = 0
        for ch in s1_hash:
            if s1_hash[ch] == s2_hash.get(ch, 0):
                matches += 1
        if matches == len(s1_hash):
            return True
        l = 0
        for i in range(len(s1), len(s2)):
            charR = s2[i]
            s2_hash[charR] = s2_hash.get(charR, 0) + 1
            if charR in s1_hash:
                if s2_hash[charR] == s1_hash.get(charR, 0):
                    matches += 1
                if s2_hash[charR] == s1_hash.get(charR, 0) + 1:
                    matches -= 1
            
            charL = s2[l]
            s2_hash[charL] -= 1
            if charL in s1_hash:
                if s2_hash[charL] == s1_hash[charL]:
                    matches += 1
                if s2_hash[charL] == s1_hash[charL] - 1:
                    matches -= 1
            l += 1
            if matches == len(s1_hash):
                return True
        return False



            