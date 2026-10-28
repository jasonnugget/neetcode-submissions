class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            prefix = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:prefix] == w2[:prefix]:
                return ""
            
            for i in range(prefix):
                if w1[i] != w2[i]:
                    chars[w1[i]].add(w2[i])
                    break

        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return not visited[char]
            
            visited[char] = True
            
            for nei in chars[char]:
                if not dfs(nei):
                    return False
            res.append(char)
            visited[char] = False
            return True

        for char in chars:
            if not dfs(char):
                return ""
        
        res.reverse()
        res = "".join(res)
        return res
