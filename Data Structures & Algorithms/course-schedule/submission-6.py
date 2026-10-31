class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            
            #proccess current class
            visit.add(course)
            prereqs = adjList[course]

            for c in prereqs:
                if not dfs(c):
                    print("hello")
                    return False
            adjList[course] = []
            visit.remove(course)
            return True
            
        

        for i in range(numCourses):
            if not dfs(i):
                print('hello2', i)
                return False
        
        return True