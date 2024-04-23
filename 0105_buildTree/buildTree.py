# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # 前序遍历的第一个值是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 在中序遍历中找到根节点的位置
        mid_idx = inorder.index(root_val)

        # 构建左子树和右子树
        root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
        root.right = self.buildTree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])

        return root


