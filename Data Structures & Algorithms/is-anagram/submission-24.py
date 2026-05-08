class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sSet = defaultdict(int)
        tSet = defaultdict(int)

        for i in s:
            sSet[i] += 1

        for j in t:
            tSet[j] += 1

        if tSet == sSet:
            return True

        else:
            return False