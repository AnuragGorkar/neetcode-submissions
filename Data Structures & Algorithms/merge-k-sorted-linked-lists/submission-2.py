# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, [lists[i].val, i])
        
        ret_node = ListNode()
        trav = ret_node

        while min_heap:
            val, i = heapq.heappop(min_heap)
            node = lists[i]
            lists[i] = node.next
            trav.next = node

            if node.next:
                heapq.heappush(min_heap, [node.next.val, i])
            node.next = None
            trav = trav.next


        return ret_node.next
        