# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def getNode(root, father):
            if root:
                fa[root] = father

                if root.val == start:
                    self.start_node = root
                getNode(root.left, root)
                getNode(root.right, root)

        fa = {}
        self.start_node = None

        getNode(root, None)

        def maxDepth(root, father):
            if not root:
                return -1

            return max(maxDepth(x, root) for x in (root.left, root.right, fa[root]) if x != father) + 1

        return maxDepth(self.start_node, self.start_node)
