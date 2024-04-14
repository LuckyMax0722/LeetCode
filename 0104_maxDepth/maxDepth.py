# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree_depth(self, root):
        if root is None:
            return 0
        else:
            left_tree = self.tree_depth(root.left)
            right_tres = self.tree_depth(root.right)
            return max(left_tree, right_tres) + 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_depth = self.tree_depth(root)
        return max_depth
