class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord('a')] += 1

            temp = tuple(temp)
            sol[temp].append(word)

        solu = []
        for key, value in sol.items():
            solu.append(value)

        return solu