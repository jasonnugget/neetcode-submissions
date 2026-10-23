class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = defaultdict(int)
        set2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            set1[s[i]] += 1
            set2[t[i]] += 1

        return set1 == set2