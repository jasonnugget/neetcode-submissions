class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        check = {'}':'{', ')':'(', ']':'['}

        for i in s:
            if len(stack) != 0 and i in check:
                popped = stack.pop()
                if check[i] != popped:
                    return False

            else:
                stack.append(i)

        return len(stack) == 0