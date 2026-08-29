class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check1 = defaultdict(int)
        check2 = defaultdict(int)

        for i in s:
            check1[i] += 1

        for j in t:
            check2[j] += 1

        return check1 == check2