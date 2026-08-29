class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 0
        most = 0
        for r in range(len(s)):
            count[s[r]] += 1
            most = max(most, count[s[r]])
            while (r - l + 1) - most > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res

