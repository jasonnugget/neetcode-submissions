class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):

            l, r = i, i
            while l <= r:
                if r >= len(s) or l < 0 or s[l] != s[r]:
                    break

                if resLen < r - l + 1:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                
                l -= 1
                r += 1

            l, r = i, i + 1
            while l < r:
                if r >= len(s) or l < 0 or s[l] != s[r]:
                    break

                if resLen < r - l + 1:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                
                l -= 1
                r += 1

        return res