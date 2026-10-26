class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = {i:[] for i in range(n)}

        for key, val in edges:
            visit[key].append(val)
            visit[val].append(key)

        visited = set()
        def dfs(key, prev):
            if key != prev and key in visited:
                return False
            
            visited.add(key)
            for k in visit[key]:
                if k == prev:
                    continue
                if not dfs(k, key):
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n     
        