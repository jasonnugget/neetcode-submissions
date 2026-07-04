class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))
            encoded += '#'
            encoded += word
        return encoded

    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            count = ''
            while s[i] != '#':
                count += s[i]
                i += 1
            count = int(count)
            word = ""
            i += 1
            for j in range(count):
                word += s[i]
                i += 1
            
            sol.append(word)

        return sol

