class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in '([{':
                stack += ch
            else:
                if not stack or closers[ch] != stack.pop():
                    return False
        return not stack