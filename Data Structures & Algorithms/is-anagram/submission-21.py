class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSeen = {}
        tSeen = {}

        for j in s:
            if j in sSeen:
                sSeen[j] += 1
            else:
                sSeen[j] = 1

        for m in t:
            if m in tSeen:
                tSeen[m] += 1
            else:
                tSeen[m] = 1

        if sSeen == tSeen:
            return True
        else:
            return False
