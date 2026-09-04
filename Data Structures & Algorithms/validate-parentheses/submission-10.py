class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        checker = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in checker:
                if not arr or arr.pop() != checker[i]:
                    return False

            else:
                arr.append(i)

        return not arr 