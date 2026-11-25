class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.n = n

        #initialize for all nodes
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        #first get the parent
        par = self.parent[x]

        #next check up the tree and path compress.
        while par != self.parent[par]:
            #while this iterates we know that par is different its parent
            #This makes it so par's parent is now its grandparent so we are skipping a node. 
            self.parent[par] = self.parent[self.parent[par]]
            #iterate par up one generation
            par = self.parent[par]
        
        return par
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        
        #otherwise we can do union by rank
        p1, p2 = self.find(x), self.find(y)

        if self.rank[p1] > self.rank[p2]:
            #p1 has a greater rank so we need to merge p2 into p1
            #to do this p1 will be p2's parent
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            #the ranks are the same. just absorb one and then increase the rank of the new parent
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True
    def getNumComponents(self) -> int:
        parentSet = set()
        for i in range(self.n):
            parentSet.add(self.find(i))
        
        return len(parentSet)

