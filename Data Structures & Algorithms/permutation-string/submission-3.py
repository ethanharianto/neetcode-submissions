class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        """
        s1_arr = [0] * 26
        s2_arr = [0] * 26
        n = len(s1)
        if n > len(s2):
            return False

        for i in range(n):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i, j in zip(s1_arr, s2_arr):
            if i == j:
                matches += 1
        
        i = 0
        for j in range(n, len(s2)):
            if matches == 26:
                return True
            index = ord(s2[j]) - ord('a')
            s2_arr[index] += 1

            if s2_arr[index] == s1_arr[index]:
                matches += 1
            
            elif s2_arr[index] == s1_arr[index] + 1:
                matches -= 1
            
            index = ord(s2[i]) - ord('a')
            s2_arr[index] -= 1
            if s2_arr[index] == s1_arr[index]:
                matches += 1
            
            elif s2_arr[index] == s1_arr[index] - 1:
                matches -= 1
            i += 1
        return matches == 26

            