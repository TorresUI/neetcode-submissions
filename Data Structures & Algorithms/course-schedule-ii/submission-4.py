class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)
        
        visit = set()
        res = []

        def dfs(crs):
            if crs in visit:
                return False
            
            if crs in res:
                return True
            
            #otherwise crs needs to be processed.
            visit.add(crs)
            prereqs = adjList[crs]

            for i in prereqs:
                if not dfs(i):
                    return False
            
            #otherwise all prereqs are complete
            adjList[crs] = []
            res.append(crs)
            visit.remove(crs)
            return True

        for i in range(numCourses):
            if i not in res and not dfs(i):
                #Found a cycle
                return []
        return res