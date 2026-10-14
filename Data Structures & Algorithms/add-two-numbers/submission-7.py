# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode()
        head = dummyNode



        while l1 or l2 or carry:

            
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            sumVal = l1Val + l2Val + carry
            newVal = sumVal % 10

            if sumVal >= 10:
                carry = 1
            else:
                carry = 0

            newNode = ListNode(newVal)
            head.next = newNode
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummyNode.next