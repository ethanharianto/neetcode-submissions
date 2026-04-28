class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stash = defaultdict(list)
        for string in strs:
            stash[tuple(sorted(string))].append(string)
        return stash.values()