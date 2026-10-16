# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        q.append(root)

        if not root:
            return res

        while q:
            res.append(q[-1].val)

            for i in range(len(q)):
                parentNode = q.popleft()

                if parentNode and parentNode.left:
                    q.append(parentNode.left)
                if parentNode and parentNode.right:
                    q.append(parentNode.right)
                        
        return res