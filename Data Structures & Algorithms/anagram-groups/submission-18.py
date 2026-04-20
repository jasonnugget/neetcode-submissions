class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for a in strs:

            count = [0] * 26

            for b in a:
                count[ord(b) - ord('a')] += 1

            res[tuple(count)].append(a)

        return list(res.values())
