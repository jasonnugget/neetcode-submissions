class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isAlpha(c):
            if ord("A") <= ord(c) <= ord("Z"):
                return True

            elif ord("a") <= ord(c) <= ord("z"):
                return True

            elif ord("0") <= ord(c) <= ord("9"):
                return True

            else:
                return False

        i = 0
        j = len(s) - 1

        while(i < j):
            while(i < j and not isAlpha(s[i])):
                i += 1
            
            while(i < j and not isAlpha(s[j])):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True