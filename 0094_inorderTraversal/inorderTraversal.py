# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def getNode(root):
            if root:
                getNode(root.left)
                res.append(root.val)
                getNode(root.right)

        res = []
        getNode(root)

        return res