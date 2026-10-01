# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode, currNode = ListNode(), ListNode()
        dummyNode = currNode

        while list1 or list2:

            if not list1:
                currNode.next = list2
                break
            
            if not list2:
                currNode.next = list1
                break

            print(currNode.val)
            if list1.val > list2.val:
                currNode.next = list2
                currNode = currNode.next
                list2 = list2.next
            else:
                currNode.next = list1
                currNode = currNode.next
                list1 = list1.next
        
        return dummyNode.next
