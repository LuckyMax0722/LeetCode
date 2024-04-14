# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_depth(self, root):
        if root is None:
            return 0
        else:
            left_tree = self.get_depth(root.left)
            right_tres = self.get_depth(root.right)

            if abs(left_tree - right_tres) > 1:
                self.status = False

            return max(left_tree, right_tres) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.status = True

        if root is None:
            return True
        else:
            self.get_depth(root)
            return self.status



