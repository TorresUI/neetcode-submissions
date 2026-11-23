"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #make a hashmap that maps the old node to the new node
        #go through the list once making new nodes and adding them to the map.
        p1 = head
        oldNodeToNew = {}

        while p1:
            newNode = Node(p1.val)
            oldNodeToNew[p1] = newNode

            p1 = p1.next

        #go through the list a second time this time adding the pointers and referencing the nodes through the map.
        p1 = head
        while p1:
            newNode = oldNodeToNew[p1]
            newNode.next = oldNodeToNew[p1.next] if p1.next else None
            newNode.random = oldNodeToNew[p1.random] if p1.random else None

            p1 = p1.next
        
        return oldNodeToNew[head] if head else None

