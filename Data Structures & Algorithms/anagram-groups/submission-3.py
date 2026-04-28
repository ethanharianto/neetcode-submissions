class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stack = defaultdict(list) # default value dictionary

        for s in strs:
            letters = [0] * 26
            for ch in s:
                letters[ord(ch) - ord('a')] += 1
            stack[tuple(letters)].append(s)
        return stack.values()

