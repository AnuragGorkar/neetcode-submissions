class Node: 
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DLL: 
    def __init__(self, capacity):
        self.root = None
        self.top = None
        self.size = 0 
        self.capacity = capacity
    
    def insert(self, node):
        node.prev = None
        node.next = None
        if self.top:
            self.top.next = node
            node.prev = self.top
        self.top = node
        self.size += 1
        if not self.root: 
            self.root = node
        if self.size > self.capacity:
            retVal = self.root.key
            self.root = self.root.next
            if self.root:
                self.root.prev = None
            self.size -= 1
            return retVal
        return None

    def remove(self, node): 
        if node == self.root: 
            self.root = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next: 
            node.next.prev = node.prev
        if node == self.top:
            self.top = node.prev
        node.prev = node.next = None
        self.size -= 1

class LRUCache:
    def __init__(self, capacity: int):
        self.dll = DLL(capacity)
        self.nodeMap = dict()
        
    def get(self, key: int) -> int:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.dll.remove(node)
            self.dll.insert(node)
            return node.val
        return -1
        
    def put(self, key: int, val: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = val
            self.dll.remove(node)
            self.dll.insert(node)
        else: 
            node = Node(val, key)
            self.nodeMap[key] = node
            retVal = self.dll.insert(node)
            if retVal is not None:
                del self.nodeMap[retVal]
