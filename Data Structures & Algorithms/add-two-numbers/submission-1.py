# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def revList(head):
            if not head: 
                return None
            p, q = head, ListNode()
            while p:
                p.next, q, p = q, p, p.next
            head.next = None
            return q

        node_sum = 0
        node_carry = 0
        prev_sum_dummy = ListNode()
        while l1 and l2: 
            node_sum = l1.val + l2.val + node_carry
            node_carry, node_sum, l1, l2 = node_sum//10, node_sum%10, l1.next, l2.next 
            prev_sum_dummy.val = node_sum
            prev_sum_dummy = ListNode(next = prev_sum_dummy)

        while l1: 
            node_sum = l1.val + node_carry
            node_carry, node_sum, l1 = node_sum//10, node_sum%10, l1.next 
            prev_sum_dummy.val = node_sum
            prev_sum_dummy = ListNode(next = prev_sum_dummy)

        while l2: 
            node_sum = l2.val + node_carry
            node_carry, node_sum, l2 = node_sum//10, node_sum%10, l2.next 
            prev_sum_dummy.val = node_sum
            prev_sum_dummy = ListNode(next = prev_sum_dummy)
        
        if node_carry: 
           prev_sum_dummy.val = node_carry
           prev_sum_dummy = ListNode(next = prev_sum_dummy) 
        
        return revList(prev_sum_dummy.next)
        