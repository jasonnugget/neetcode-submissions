class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        for i, j in enumerate(s):
            lastSeen[j] = i

        size, end = 0, 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastSeen[c])

            if i == end:
                res.append(size)
                size = 0

        return res