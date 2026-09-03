class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ender = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for i in s:
            if i in ender:
                if not stack or stack.pop() != ender[i]:
                    return False

            else:
                stack.append(i)

        return not stack