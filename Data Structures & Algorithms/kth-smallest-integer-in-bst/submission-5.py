# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #want to do in order traversal where we explore left then current then right. At each step we will decrement nodes seen and then when k = 0 we return the current node
        arr = []

        def dfs(root):       
            nonlocal k
            if not root:
                return
            
            #first process the left
            dfs(root.left)
            #then process current
            arr.append(root.val)      
            #then process right
            dfs(root.right)
        dfs(root)
        
        return arr[k-1]