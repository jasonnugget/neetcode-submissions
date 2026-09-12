class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded = encoded + str(len(word)) + '#' + word\
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        temp = 0
        while temp < len(s):
            count = ''
            while s[temp] != '#':
                count += s[temp]
                temp += 1

            count = int(count)

            word = ''
            for i in range(count):
                temp += 1
                word += s[temp]

            res.append(word)
            temp += 1

        return res