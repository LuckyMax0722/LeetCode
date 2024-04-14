# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    '''
    def get_tree(self, root):
        if root is None:
            return 0
        else:
            self.num = self.num + 1
            left_tree = self.get_tree(root.left)
            right_tree = self.get_tree(root.right)
            return max(left_tree, right_tree) + 1

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.num = 0

        self.get_tree(root)

        return self.num
    '''

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
