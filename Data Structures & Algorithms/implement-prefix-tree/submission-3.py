class Node:
    def __init__(self):
        #Map each letter to the node 
        self.neighbors = {}
        #boolean to represent end of word
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        #check if the node exists if it does traverse to it. 
        #if it doesnt create a node and then traverse into it
        curr = self.root
        for c in word:
            if c not in curr.neighbors:
                #making a new node for that char
                curr.neighbors[c] = Node()
            #Traversing to the next letter
            curr = curr.neighbors[c]
        
        #set the end of the word
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        #traverse through neighbors and if c is not in neighbors return false.
        curr = self.root
        for c in word:
            if c not in curr.neighbors:
                return False
            curr = curr.neighbors[c]
        
        #Check to see if its the end of a word
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.neighbors:
                return False
            curr = curr.neighbors[c]
        
        return True        
        