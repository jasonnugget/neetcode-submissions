class Solution:
    def isValid(self, s: str) -> bool:
        checker = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for i in s:
            if i in checker:
                if not stack or checker[i] != stack.pop():
                    return False

            else:
                stack.append(i)

        return not stack