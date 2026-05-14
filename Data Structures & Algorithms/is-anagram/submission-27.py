class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        check1 = defaultdict(int)
        check2 = defaultdict(int)

        for letters in s:
            check1[letters] += 1

        for letters in t:
            check2[letters] += 1

        if check1 == check2:
            return True

        return False