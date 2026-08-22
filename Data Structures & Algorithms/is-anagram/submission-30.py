class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = defaultdict(int)
        set2 = defaultdict(int)

        for i in s:
            set1[i] += 1

        for j in t:
            set2[j] += 1

        return set1 == set2