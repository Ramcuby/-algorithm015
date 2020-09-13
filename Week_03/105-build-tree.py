# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def bdTree(p_l: int, p_r: int, i_l: int, i_r: int):
            if p_l > p_r: return None
            p_root = p_l
            i_root = index[preorder[p_root]]
            root = TreeNode(preorder[p_root]) # 根节点
            size_left = i_root - i_l # 得到左子树中的节点数目
            root.left = bdTree(p_l + 1, p_l + size_left, i_l, i_root - 1)
            root.right = bdTree(p_l + size_left + 1, p_r, i_root + 1, i_r)
            return root
        
        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}# 构造哈希映射，定位根节点
        return bdTree(0, n - 1, 0, n - 1)

