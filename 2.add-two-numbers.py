#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_number(l: Optional[ListNode]) -> int:
            num=0
            factor=1
            while l:
                num=num+l.val*factor
                factor*=10
                l=l.next
            return num
        def number_to_list(n:int) -> Optional[ListNode]:
            head=ListNode(0)
            p=head
            while n>=10:
                p.val=n%10
                p.next=ListNode(0)
                p=p.next
                n//=10
            p.val=n
            return head
        l=list_to_number(l1)+list_to_number(l2)
        return number_to_list(l)
        
# @lc code=end

