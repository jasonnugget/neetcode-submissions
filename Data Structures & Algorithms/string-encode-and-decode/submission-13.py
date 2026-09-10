class Solution:

    def encode(self, strs: List[str]) -> str:
        words = ''
        for word in strs:
            words = words + str(len(word)) + '#' + word

        return words 
    def decode(self, s: str) -> List[str]:
        trav = 0
        res = []
        while trav < len(s):
            temp = ''
            while s[trav] != '#':
                temp += s[trav]
                trav += 1

            temp = int(temp)
            word = ''
            for i in range(temp):
                trav += 1
                word += s[trav]

            trav += 1
            res.append(word)

        return res



