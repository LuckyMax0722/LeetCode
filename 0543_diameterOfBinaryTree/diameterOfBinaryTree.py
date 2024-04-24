# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -1
            l_left = dfs(root.left) + 1
            l_right = dfs(root.right) + 1
            self.ans = max(self.ans, l_left + l_right)
            return max(l_left, l_right)

        self.ans = 0
        dfs(root)
        return self.ans