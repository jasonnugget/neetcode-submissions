class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            tracker[tuple(key)].append(word)

        return list(tracker.values())