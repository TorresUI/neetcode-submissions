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
        oldToNew = {}

        tempHead = head

        while tempHead:
            newNode = Node(tempHead.val)
            oldToNew[tempHead] = newNode
            tempHead = tempHead.next
        
        tempHead = head

        while tempHead:
            newNode = oldToNew[tempHead]
            newNode.next = oldToNew[tempHead.next] if tempHead.next else None
            newNode.random = oldToNew[tempHead.random] if tempHead.random else None
            tempHead = tempHead.next

        return oldToNew[head] if head else None
