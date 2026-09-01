class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        for word in strs:
            coded = coded + str(len(word)) + '#' + word

        return coded

    def decode(self, s: str) -> List[str]:
        res = []
        travel = 0

        while travel < len(s):
            word = ''
            temp = ''
            while s[travel] != '#':
                temp = temp + s[travel]
                travel += 1

            temp = int(temp)

            for i in range(temp):
                travel += 1
                word = word + s[travel]
            
            travel += 1

            res.append(word)

        return res