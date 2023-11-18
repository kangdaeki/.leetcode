#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev=-sys.maxsize
    next=sys.maxsize
    mindiff=sys.maxsize
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node: Optional[TreeNode]):
            if None!=node.left:
                inorder(node.left)
            self.next=node.val
            if self.mindiff>(self.next-self.prev):
                self.mindiff=self.next-self.prev
            self.prev=self.next
            if None!=node.right:
                inorder(node.right)
            return
        inorder(root)
        return self.mindiff
            
# @lc code=end

