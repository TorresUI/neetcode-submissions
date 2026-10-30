class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        classes = {}

        for i in range(numCourses):
            classes[i] = []
        
        for a, b in prerequisites:
            classes[a].append(b)
        visit = set()
        cycle = set()
        res = []
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            #process this class
            cycle.add(c)
            prereqs = classes[c]

            for i in prereqs:
                if not dfs(i):
                    return False
            visit.add(c)
            res.append(c)
            cycle.remove(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []        
        return res
        