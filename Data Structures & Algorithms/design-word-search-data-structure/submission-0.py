class Node: 
    def __init__(self): 
        self.is_end = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node.children[ord(char)-97]:
                node.children[ord(char)-97] = Node()
            node = node.children[ord(char)-97]
        node.is_end = True 

    def search(self, word: str) -> bool:
        def dfs(node, word, index):
            if not node: 
                return False
            elif index==len(word): 
                return node.is_end
            else: 
                if word[index] != '.': 
                    return dfs(node.children[ord(word[index])-97], word, index+1)
                else: 
                    for child in node.children: 
                        if dfs(child, word, index+1): 
                            return True
                    return False
        
        return dfs(self.root, word, 0)







        
