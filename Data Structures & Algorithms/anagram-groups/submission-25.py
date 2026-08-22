class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = dict()
        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord('a')] += 1

            temp = tuple(temp)
            if temp in sol:
                sol[temp].append(word)
            else:
                sol[temp] = [word]
            
        solution = []
        for key in sol:
            solution.append(sol[key])

        return solution