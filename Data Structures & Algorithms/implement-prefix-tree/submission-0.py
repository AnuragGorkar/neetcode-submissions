class Node: 
    children = []
    def __init__(self): 
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word: 
            if not node.children[ord(char)-97]:
                node.children[ord(char)-97] = Node() 
            node = node.children[ord(char)-97] 
        node.isEnd = True
                
    def search(self, word: str) -> bool:
        node = self.root
        for char in word: 
            if not node.children[ord(char)-97]:
                return False
            node = node.children[ord(char)-97] 
        return node.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix: 
            if not node.children[ord(char)-97]:
                return False
            node = node.children[ord(char)-97] 
        return True
        
        