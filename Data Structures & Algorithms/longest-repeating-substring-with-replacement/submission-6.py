class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        tracker = defaultdict(int)
        freq = 0
        res = 0
        while r < len(s):
            tracker[s[r]] += 1
            freq = max(freq, tracker[s[r]])
            if (r - l + 1) - freq > k:
                tracker[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
            
        return res