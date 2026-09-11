class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        tracker = {}
        res = 0
        while r < len(s):
            if s[r] in tracker and tracker[s[r]] >= l:
                l = tracker[s[r]] + 1
            
            tracker[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res