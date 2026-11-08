class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(set)

        for course, prereq in prerequisites:
            adjList[prereq].add(course)
        
        seen = set()
        path = set()
        res = []

        def dfs(course):
            if course in path:
                return False

            if course in seen:
                return True

            path.add(course)

            if course in adjList:
                for nei in adjList[course]:
                    if not dfs(nei):
                        return False
            
            path.remove(course)
            seen.add(course)
            res.append(course)
            return True

        for keys in adjList:
            if not dfs(keys):
                return []

        res.reverse()

        for i in range(numCourses):
            if i not in seen:
                res.append(i)

        return res

        

        