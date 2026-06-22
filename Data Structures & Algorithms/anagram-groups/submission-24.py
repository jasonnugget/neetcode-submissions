class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for words in strs:
            word = [0] * 26
            for i in words:
                word[ord(i) - ord("a")] += 1
            if tuple(word) not in result:
                result[tuple(word)] = []
                result[tuple(word)].append(words)
            else:
                result[tuple(word)].append(words)

        printResult = []
        for myDict in result.values():
            printResult.append(myDict)
        
        return printResult

            