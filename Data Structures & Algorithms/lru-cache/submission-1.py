class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        #initialize the two pointers to be LRU and MRU and point to each other
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        #remove and reinsert the key in the list so that way we move it to MRU
        keyNode = self.cache[key]
        self.remove(keyNode)
        self.insert(keyNode)
        return keyNode.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #Need to update the value and perform remove / insert
            keyNode = self.cache[key]
            keyNode.value = value

            self.remove(keyNode)
            self.insert(keyNode)
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.insert(newNode)
        
        #Now we need to check if the capacity has been exceeded
        isCapExceeded = len(self.cache) > self.cap
        
        if isCapExceeded:
            #need to remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        self.right.prev = node

        node.prev = temp
        node.next = self.right

