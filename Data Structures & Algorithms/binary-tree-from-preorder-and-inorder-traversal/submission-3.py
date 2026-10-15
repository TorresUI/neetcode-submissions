# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        #first we need a map of inorder since we are searching in inorder array
        self.inorderMap = {}
        self.preorderIndex = 0
        for index, value in enumerate(inorder):
            self.inorderMap[value] = index
        
        def dfs(l, r):
            if l > r:
                return None
            
            #we want to get the value of the current node
            rootval = preorder[self.preorderIndex]
            self.preorderIndex += 1

            #Make a new node to represent the root of the subtree
            root = TreeNode(rootval)
            #Need to find the left and right subArray's to construct the left and right nodes as well.
            #First we need to find where in the inorder array the current root node is
            rootIndex = self.inorderMap[rootval]

            #Now that we have the root val in the inorder. Everything to the left is part of the left subtree so l - m - 1 and for the right it is m + 1 -> r

            root.left = dfs(l, rootIndex - 1)
            root.right = dfs(rootIndex + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)
