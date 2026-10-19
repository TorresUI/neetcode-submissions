# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderMap = {}
        for index, value in enumerate(inorder):
            self.inorderMap[value] = index
        
        #Now we can look up in inorder using O(1)
        self.preorderIndex = 0
        def dfs(l, r):
            #maintaining left and right pointer to identify subArray for inorderArray.
            #index for preorder will always just increment. first it is the root next it is the left subtree and then the right subtree
            if l > r:
                return None
            val = preorder[self.preorderIndex]
            self.preorderIndex += 1

            newNode = TreeNode(val)
            m = self.inorderMap[val]

            newNode.left = dfs(l, m - 1)
            newNode.right = dfs(m + 1, r)
            return newNode
        return dfs(0, len(inorder) - 1)
