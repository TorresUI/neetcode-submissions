class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False



class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            #Check if this character is not in children set
            #if it is then we just move onto the next one
            #if it is not then we need to add it to the children set
            if char not in curr.children:
                #Create a new node for that letter
                curr.children[char] = Node()
            
            #iterate the node pointer down the tree
            curr = curr.children[char]
        
        #Now curr is the final node in the word. We need to mark it as the end of word
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        
        