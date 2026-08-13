# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                nodes.append("#")
                continue
            nodes.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        if nodes[0] == "#":
            return None
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            left = nodes[i]
            if left != "#":
                node.left = TreeNode(int(left))
                q.append(node.left)
            right = nodes[i+1]
            if right != "#":
                node.right = TreeNode(int(right))
                q.append(node.right)
            i += 2
        return root