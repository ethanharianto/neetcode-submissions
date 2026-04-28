class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for ch in s:
                letters[ord(ch) - ord('a')] += 1 
            anagrams[tuple(letters)].append(s)
        
        return list(anagrams.values())