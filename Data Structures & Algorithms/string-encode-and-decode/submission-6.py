class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{str(len(word))}:{word}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        l = 0
        sol = []

        while l < len(s):
            count = ""
            while s[l] != ':':
                count += s[l]
                l += 1
            l += 1
            count = int(count)

            word = ""
            for i in range(count):
                word += s[l]
                l += 1
            sol.append(word)
        return sol
            
