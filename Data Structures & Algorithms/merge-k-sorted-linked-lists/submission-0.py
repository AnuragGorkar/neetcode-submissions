# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        heapq.heapify(min_heap)
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        head, prev = None, None
        while len(min_heap):
            min_node_val, index, min_node = heapq.heappop(min_heap)
            if not head:
                head, prev = min_node, min_node
            else:
                prev.next, prev = min_node, min_node
            if min_node.next:
                heapq.heappush(min_heap, (min_node.next.val, index, min_node.next))
        if prev:
            prev.next = None
        return head    