class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = defaultdict(int)

        for n in s:
            set1[n] += 1

        set2 = defaultdict(int)
        
        for n in t:
            set2[n] += 1


        return set1 == set2
