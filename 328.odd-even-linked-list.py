class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None: 
            return head
        odd=head
        if head.next==None:
            return head
        even_head=head.next
        even=even_head
        while even:
            odd.next=even.next
            prev=odd
            odd=odd.next
            if odd:
                even.next=odd.next
                even=even.next
                if even==None:
                    odd.next=even_head
            else:
                prev.next=even_head
                break
        return head
