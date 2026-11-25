class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Want to use union find to count the number of connected components. 

        parent = {}
        rank = {}

        #initialize parents and ranks for each of the nodes in the problem.
        for i in range(n):
            parent[i] = i
            rank[i] = 0

        #we want to go through each edge and perform a union on the two nodes. To do that we must find their parent and then merge by rank.

        def find(x):
            #take a node and find its parents
            par = parent[x]
            while par != parent[par]:
                #while par doesnt equal its parent then we have to increment up but we can also path compress given that we have not found the true parent yet
                #We are setting par's parent to its grandparent 
                parent[par] = parent[parent[par]]
                #iterating par up the tree
                par = parent[par]
            
            return par
        
        def union(x, y):
            nonlocal n
            p1, p2 = find(x), find(y)

            if p1 == p2:
                #Early return for a cycle / already unioned part
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                #both are equal
                parent[p2] = p1
                rank[p1] += 1
            n -= 1
        
        #now we go through all of the edges. and union them. THen return the n after it has been decremented by the amount of unions
        for x, y in edges:
            union(x, y)
        
        return n

