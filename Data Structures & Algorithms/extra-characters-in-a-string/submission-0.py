from functools import lru_cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

class Solution:
    def minExtraChar(self, s, dictionary):
        n = len(s)

        # Build trie from dictionary
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        @lru_cache(None)
        def dfs(i: int) -> int:
            """Return min extra chars starting from index i"""
            if i == n:
                return 0

            # Option 1: skip s[i]
            res = 1 + dfs(i + 1)

            # Option 2: follow trie and match words
            node = trie.root
            for j in range(i, n):
                ch = s[j]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end:
                    res = min(res, dfs(j + 1))

            return res

        return dfs(0)