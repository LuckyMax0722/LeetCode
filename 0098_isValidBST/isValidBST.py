# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left=-inf, right=inf):
            if not root:
                return True
            x = root.val

            return left < x < right and dfs(root.left, left, x) and dfs(root.right, x, right)

        return dfs(root, -inf, inf)