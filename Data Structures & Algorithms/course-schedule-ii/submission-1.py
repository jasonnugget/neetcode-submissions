class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(set)

        for course, prereq in prerequisites:
            adjList[prereq].add(course)
        
        seen = set()
        path = set()
        res = []

        def dfs(course):
            if course not in adjList:
                res.append(course)
                return True

            if course in path:
                return False

            if course in seen:
                return True

            path.add(course)

            
            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            
            path.remove(course)
            seen.add(course)
            res.append(course)
            return True

        res.reverse()

        for i in range(numCourses):
            if not dfs(i):
                return []

        res.reverse()
        return res

        

        