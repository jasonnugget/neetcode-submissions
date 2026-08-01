class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = defaultdict(int), defaultdict(int)

        for c in t:
            countT[c] += 1

        res, resLen = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            index = s[r]
            window[index] += 1
            if index in countT and window[index] == countT[index]:
                have += 1

            if have == need:

                while (have == need):
                    if r - l + 1 <resLen:
                        resLen = r - l + 1
                        res = [l, r]
                    if s[l] in countT and window[s[l]] == countT[s[l]]:
                        window[s[l]] -= 1
                        have -= 1
                    else:
                        window[s[l]] -= 1
                    l += 1

        
        if resLen == float("infinity"):
            return ''

        else:
            return s[res[0]:res[1]+1]

            
            
            

            