class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{str(len(word))}:{word}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        sol = []

        while r < len(s):
            while s[r] != ':':
                r += 1
            
            count = ""
            while s[l] != ':':
                count += s[l]
                l += 1
            r += 1
            count = int(count)

            word = ""
            for i in range(count):
                word += s[r]
                r += 1
            sol.append(word)
            l = r
        return sol
            
