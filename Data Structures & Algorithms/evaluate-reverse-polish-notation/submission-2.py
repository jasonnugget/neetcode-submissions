class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '-':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif char == '/':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(char))

        return stack[-1]