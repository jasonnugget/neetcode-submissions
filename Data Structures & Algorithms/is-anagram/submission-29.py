class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        list1 = defaultdict(int)
        list2 = defaultdict(int)

        for i in range(len(s)):
            list1[s[i]] += 1
            list2[t[i]] += 1

        return list1 == list2
