class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        checker = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in checker and arr:
                if arr[-1] != checker[i]:
                    return False
                arr.pop()

            else:
                arr.append(i)

        return not arr 