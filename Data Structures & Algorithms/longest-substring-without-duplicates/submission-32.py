class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        checker = defaultdict(int)
        for r in range(len(s)):
            if s[r] in checker and l <= checker[s[r]]:
                l = checker[s[r]] + 1

            checker[s[r]] = r
            res = max(res, r - l + 1)

        return res 