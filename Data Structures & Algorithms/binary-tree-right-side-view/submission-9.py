# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs where we only consider the right most node at every step
        q = collections.deque()
        q.append(root)
        res = []

        if not root:
            return []
        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                currNode = q.popleft()
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
        
        return res