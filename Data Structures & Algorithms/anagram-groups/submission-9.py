class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            letters = [0] * 26
            for l in s:
                letters[ord(l) - ord('a')] += 1
            hashmap[tuple(letters)].append(s)
        
        return hashmap.values()

        