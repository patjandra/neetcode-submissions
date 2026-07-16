# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(rt, st):
            if not rt and not st:
                return True
            elif rt and st and rt.val == st.val:
                return isSameTree(rt.left, st.left) and isSameTree(rt.right, st.right)
            return False
        
        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)