class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = {i:[] for i in range(n)}
        for i,j in edges:
            nodes[i].append(j)
            nodes[j].append(i)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for nei in nodes[node]:
                dfs(nei)


        res = 0
        for i in range(n):
            if i in visited:
                continue

            dfs(i)
            res += 1
        
        return res