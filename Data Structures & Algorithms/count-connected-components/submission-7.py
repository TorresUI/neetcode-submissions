class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = []
        for i in range(n):
            par.append(i)
        rank = [1] * n

        def find(node):
            #Need to return the nodes parent
            if node == par[node]:
                return node
            
            #otherwise we need to recursively find the parent
            parent = find(par[node])
            return parent
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if rank[p1] > rank[p2]:
                #r2 gets absorbed
                par[p2] = p1
                rank[p1] += rank[p2]
                return p1
            else:
                #r1 gets absorbed
                par[p1] = p2
                rank[p2] += rank[p1]
                return p2


        for n1, n2 in edges:
            union(n1, n2)

        parents = set()
        for i in range(n):
            parent = find(i)
            if parent not in parents:
                parents.add(parent)
        
        return len(parents)