# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if root:
                dfs(root.left)
                self.ans.append(root.val)
                dfs(root.right)

        self.ans = []
        dfs(root)

        return self.ans[k-1]
    '''

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root or self.k == 0:
                return
            if root:
                dfs(root.left)
                self.k -= 1
                if self.k == 0:
                    self.res = root.val
                    return
                dfs(root.right)

        self.k = k
        self.res = 0
        dfs(root)
        return self.res

        return self.ans[k - 1]
