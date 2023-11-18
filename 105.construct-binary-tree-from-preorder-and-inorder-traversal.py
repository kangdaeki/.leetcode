#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if 0<len(preorder):
            for i in range(len(inorder)):
                if preorder[0]==inorder[i]:
                    return TreeNode(preorder[0],self.buildTree(preorder[1:i+1],inorder[0:i]),self.buildTree(preorder[i+1:],inorder[i+1:]))
# @lc code=end

