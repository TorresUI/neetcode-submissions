class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        classes = {}
        for i in range(numCourses):
            classes[i] = []
        
        for a, b in prerequisites:
            classes[a].append(b)
        
        visit = set()
        
        def dfs(c):
            if c in visit:
                print(c)
                return False

            if len(classes[c]) == 0:
                return True
            
            #otherwise process the current class and dfs its prereqs
            prereqs = classes[c]
            visit.add(c)
            for i in prereqs:
                if not dfs(i):
                    return False
            visit.remove(c)
            classes[c] = []
            return True
        
        #Now run DFS on all courses. If there are any with a circular dependency return false
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True