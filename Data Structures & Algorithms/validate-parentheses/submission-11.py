class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tracker = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for char in s:
            if char in tracker:
                if not stack or stack.pop() != tracker[char]:
                    return False

            else:
                stack.append(char)
            
        return not stack