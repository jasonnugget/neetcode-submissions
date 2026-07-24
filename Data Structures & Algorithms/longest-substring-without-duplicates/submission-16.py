class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in check:
                l = max(l, check[s[r]] + 1)
                check[s[r]] = r

            check[s[r]] = r
            res = max(res, r - l + 1)

        return res
