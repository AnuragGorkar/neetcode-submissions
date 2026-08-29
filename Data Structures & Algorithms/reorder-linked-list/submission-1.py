# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head): 
        if not head: 
            return head
        else: 
            p, q = head, None
            while p: 
                p.next, q, p = q, p, p.next
            return q

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return
        slow, fast = ListNode(-1, head), head
        while fast and fast.next: 
            slow, fast = slow.next, fast.next.next
        p1, p2, slow.next = head, self.reverseList(slow.next), None
        while p1 and p2:
            p1.next, p2.next, p1, p2 = p2, p1.next if p1.next else p2.next, p1.next, p2.next 










        