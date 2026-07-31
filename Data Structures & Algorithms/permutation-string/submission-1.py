class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1array = [0] * 26
        s2array = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1array[ord(s1[i]) - ord('a')] += 1
            s2array[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1array[i] == s2array[i]:
                matches += 1

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2array[index] += 1
            if s2array[index] == s1array[index]:
                matches += 1
            elif s2array[index] == s1array[index] + 1:
                 matches -= 1

            index = ord(s2[l]) - ord('a')
            s2array[index] -= 1
            if s2array[index] == s1array[index]:
                matches += 1
            elif s2array[index] == s1array[index] - 1:
                matches -= 1
            
            l += 1

        return matches == 26