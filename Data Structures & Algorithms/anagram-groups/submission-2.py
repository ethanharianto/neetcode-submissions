class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stack = defaultdict(list)
        for word in strs:
            letters = [0] * 26
            for ch in word:
                letters[ord(ch) - ord('a')] += 1
            stack[tuple(letters)].append(word)
        return stack.values()