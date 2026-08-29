# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, trav = 0, head
        while trav: 
            trav = trav.next
            count+=1
        index_to_remove = count-n-1
        trav = head
        if index_to_remove<0: 
            head = head.next
        else: 
            while index_to_remove>0: 
                trav = trav.next
                index_to_remove-=1
            trav.next = trav.next.next
        return head
        
        