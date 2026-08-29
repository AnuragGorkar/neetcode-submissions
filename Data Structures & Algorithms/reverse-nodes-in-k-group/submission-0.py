# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        p, q = head, None
        while p:
            p.next, q, p = q, p, p.next 
        return q, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        trav, rev_head, rev_tail, prev_node = head, None, None, dummy_head
        
        while trav != None:
            i = 1
            while i<k and trav.next:
                trav = trav.next 
                i += 1
            if i<k:
                break
            next_node, trav.next  = trav.next, None

            rev_head, rev_tail = self.reverseList(prev_node.next)

            prev_node.next = rev_head
            rev_tail.next = next_node

            prev_node = rev_tail
            trav = next_node
        
        return dummy_head.next

