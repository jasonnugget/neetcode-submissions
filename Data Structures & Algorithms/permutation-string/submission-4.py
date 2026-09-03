class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checker = defaultdict(int)

        for char in s1:
            checker[char] += 1

        l = 0
        for r in range(len(s2)):
            temp = defaultdict(int)
            if s2[r] in checker:
                l = r
                temp[s2[r]] += 1
                if temp == checker:
                    return True
                r += 1
                while r < len(s2) and s2[r] in checker:
                    temp[s2[r]] += 1
                    r += 1
                    if temp == checker:
                        return True


        return False

