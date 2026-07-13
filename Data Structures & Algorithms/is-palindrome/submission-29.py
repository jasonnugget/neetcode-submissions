class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while(l < r):
            if(s[l].isalpha() != True):
                while s[l].isalnum() == False and l < r:
                    l += 1
                
            if(s[r].isalpha() != True):
                while s[r].isalnum() == False and l < r:
                    r -= 1

            if(s[r].lower() != s[l].lower()):
                return False

            l += 1
            r -= 1
            

        return True