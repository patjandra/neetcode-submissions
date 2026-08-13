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
            if nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            if nodes[i+1] != "#":
                node.right = TreeNode(int(nodes[i+1]))
                q.append(node.right)
            i += 2
        return root