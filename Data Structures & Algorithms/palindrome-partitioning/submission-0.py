class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isValidPalindrome(string):
            if len(string) == 1:
                return True

            l = 0
            r = len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False

                l += 1
                r -= 1

            return True

        def dfs(i):
            if i == len(s):
                res.append(part.copy())

            for j in range(i, len(s)):
                if isValidPalindrome(s[i:j + 1]):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

