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
            word = ""
            tempInt = ""
            while s[travel] != '#':
                tempInt += s[travel]
                travel += 1

            tempInt = int(tempInt)

            for i in range(tempInt):
                travel += 1
                word += s[travel]
            
            travel += 1
            res.append(word)

        return res


