class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        count = 0
        sol = []

        while count < len(s):
            num = ""
            while s[count] != "#":
                num = num + s[count]
                count += 1
            temp = int(num)
            word = ""
            for i in range(temp):
                count += 1
                word = word + s[count]
            
            sol.append(word)
            count += 1

        return sol
