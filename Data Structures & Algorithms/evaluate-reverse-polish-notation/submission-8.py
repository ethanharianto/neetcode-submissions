class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop() + stack.pop())
            elif ch == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(ch))
        return stack[0]