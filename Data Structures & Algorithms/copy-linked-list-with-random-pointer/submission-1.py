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
        curr = head
        oldToNew = {None: None}

        while curr:
            newNode = Node(curr.val)
            oldToNew[curr] = newNode
            curr = curr.next
        
        curr = head

        while curr:
            copyNode = oldToNew[curr]
            copyNode.next = oldToNew[curr.next]
            copyNode.random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]