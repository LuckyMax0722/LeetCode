# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        self.temp = []
        self.ans = []
        def dfs(root):
            if root:
                self.temp.append(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        self.temp.sort()
        for i in range(len(self.temp) - 1):
            self.ans.append(abs(self.temp[i] - self.temp[i+1]))

        return min(self.ans)
        '''
        self.temp = 1000000
        self.ans = 1000000

        def dfs(root):
            if root:
                dfs(root.left)
                self.ans = min(self.ans, abs(self.temp - root.val))
                self.temp = root.val
                dfs(root.right)

        dfs(root)
        return self.ans

