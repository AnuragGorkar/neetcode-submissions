"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        trav = head
        while trav:  
            new_node = Node(trav.val)
            new_node.random = trav
            new_node.next = trav.next
            trav.next = new_node
            trav = new_node.next
        trav = head
        while trav and trav.next: 
            inserted_node = trav.next
            inserted_node.random = trav.random.next if trav.random else None
            trav = trav.next.next
        trav, ret_head = head, head.next if head else None
        while trav and trav.next.next:
            inserted_node = trav.next
            trav.next =  inserted_node.next
            inserted_node.next = inserted_node.next.next if inserted_node.next else None
        if trav: 
            trav.next = None
        return ret_head


            
        
         