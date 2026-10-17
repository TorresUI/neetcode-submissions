class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.endOfWord = True        

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(index, root):
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in root.children.values():
                        if dfs(i + 1, child):
                            return True
                        
                    return False
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
                    
            
            return root.endOfWord

        return dfs(0, curr)

        
