#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_node=head
        my_list=[]
        while my_node:
            my_list.append(my_node)
            my_node=my_node.next
        my_head=ListNode()
        results=my_head
        my_len=len(my_list)
        for i in range(len(my_list)):
            results.next=my_list[my_len-1-i]
            results=results.next
        results.next=None
        return my_head.next
        
# @lc code=end

