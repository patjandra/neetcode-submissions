# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return False
            
            if isSameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        def isSameTree(tree1, tree2):
            if tree1 and tree2 and tree1.val == tree2.val:
                return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
            if not tree1 and not tree2:
                return True
            else:
                return False
        
        return dfs(root)
