class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in checker and checker[s[r]] >= l:
                l = checker[s[r]] + 1
            
            checker[s[r]] = r
            
            res = max(res, r - l + 1)

        return res