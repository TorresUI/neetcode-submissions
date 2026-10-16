# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        if not root:
            return res

        while q:
            #Whatever is in the q at the beginning of the iteration is the previous level.
            level = []
            #we need to incremenet through the q and replace all nodes with their children to progress to the next level.
            for i in range(len(q)):
                parentNode = q.popleft()
                level.append(parentNode.val)

                #We need to add the children to the q if they are not null
                if parentNode.left:
                    q.append(parentNode.left)
                if parentNode.right:
                    q.append(parentNode.right)
            
            res.append(level)

        return res