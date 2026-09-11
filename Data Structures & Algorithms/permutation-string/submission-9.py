class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        matches = 0

        checkS1 = [0] * 26
        checkS2 = [0] * 26

        for i in range(len(s1)):
            checkS1[ord(s1[i]) - ord('a')] += 1
            checkS2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if checkS1[i] == checkS2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2), 1):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            checkS2[index] += 1
            if checkS1[index] == checkS2[index]:
                matches += 1
            elif checkS1[index] + 1 == checkS2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            checkS2[index] -= 1
            if checkS1[index] == checkS2[index]:
                matches += 1
            elif checkS1[index] - 1 == checkS2[index]:
                matches -= 1

            l += 1

        return matches == 26

        