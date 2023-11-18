#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode()
        my_node=list3
        while list1 and list2:
            if list1.val<=list2.val:
                my_node.next=list1
                list1=list1.next
            else:
                my_node.next=list2
                list2=list2.next
            my_node=my_node.next
        if list1:
            my_node.next=list1
        if list2:
            my_node.next=list2
        return list3.next
            
# @lc code=end

