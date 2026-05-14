class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)
        
        for word in strs:
            alphabet = [0] * 26

            for letters in word:
                alphabet[ord(letters) - ord('a')] += 1
            
            anagrams[tuple(alphabet)].append(word)

        return list(anagrams.values())
