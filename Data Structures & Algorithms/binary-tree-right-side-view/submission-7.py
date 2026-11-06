# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque([root])
        res = []

        if not root:
            return res

        while q:
            
            for i in range(len(q)):
                #BFS
                #at each processed level add the right most element to the res array
                if i == 0:
                    res.append(q[-1].val)
                
                #otherwise 
                current = q.popleft()

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return res