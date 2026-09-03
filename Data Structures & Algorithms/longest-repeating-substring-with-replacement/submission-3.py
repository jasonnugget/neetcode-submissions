class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq = defaultdict(int)
        most = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most = max(most, freq[s[r]])
            while (r - l + 1) - most > k and l < r:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

            