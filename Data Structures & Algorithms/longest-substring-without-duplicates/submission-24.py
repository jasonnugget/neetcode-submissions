class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = {}
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if s[r] in check and l <= check[s[r]]:
                l = check[s[r]] + 1

            check[s[r]] = r
            r += 1

            res = max(res, r - l)

        return res
                
