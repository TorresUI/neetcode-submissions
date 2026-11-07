class Node:

    def __init__(self):
        self.neighbors = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root

        for i in word:
            if i not in root.neighbors:
                root.neighbors[i] = Node()
            root = root.neighbors[i]        
        #now the loop is complete we should be at the last letter
        root.endOfWord = True

    def search(self, word: str) -> bool:
        root = self.root
        #iterate through the letter
        for i in word:
            if i not in root.neighbors:
                return False
            root = root.neighbors[i]
        
        #return true only if the last letter has endOfWord = True
        return root.endOfWord
    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for i in prefix:
            if i not in root.neighbors:
                return False
            root = root.neighbors[i]
        return True

        
        