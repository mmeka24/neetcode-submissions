class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(second + first)

            elif c == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)

            elif c == '/': 
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))

            elif c == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(second * first)

            else: 
                stack.append(int(c))

        return stack[0]