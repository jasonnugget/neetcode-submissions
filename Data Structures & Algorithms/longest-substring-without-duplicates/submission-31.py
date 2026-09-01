class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in tracker and tracker[s[r]] >= l:
                l = tracker[s[r]] + 1
                tracker[s[r]] = r
            
            tracker[s[r]] = r
            res = max(res, r - l + 1)

        return res
