class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        s = list(s)
        t = list(t)

        for i in range(len(s)):
            if s[0] in t:
                t.remove(s[0])
                s.remove(s[0])

        if len(s) == 0 and len(t) == 0:
            return True
        else:
            return False