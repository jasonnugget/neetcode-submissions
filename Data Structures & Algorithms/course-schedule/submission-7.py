class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = {i:[] for i in range(numCourses)}
        for val, key in prerequisites:
            seen[val].append(key)
        
        visitedSet = set()
        def dfs(key):
            if key in visitedSet:
                return False

            if seen[key] == []:
                return True

            visitedSet.add(key)
            for nei in seen[key]:
                if dfs(nei) == False:
                    return False
            visitedSet.remove(key)
            seen[key] = []
            return True

        for key in seen:
            if not dfs(key):
                return False

        return True