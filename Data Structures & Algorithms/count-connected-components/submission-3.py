class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeList = {i:[] for i in range(n)}
        for key, val in edges:
            nodeList[key].append(val)
            nodeList[val].append(key)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in nodeList[node]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i in visited:
                continue

            dfs(i)
            res += 1

        return res