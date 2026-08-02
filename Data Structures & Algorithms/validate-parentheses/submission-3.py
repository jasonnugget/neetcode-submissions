class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        check = {'}':'{', ')':'(', ']':'['}

        for i in s:
            if i in check and len(stack) != 0:
                popped = stack.pop()
                if check[i] != popped:
                    return False

            else:
                stack.append(i)

        if len(stack) == 0:
            return True

        else:
            return False