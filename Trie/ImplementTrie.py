#class TrieNode:
#    def __init__(self):
#        self.children = {}  # Dictionary to store child nodes.
#        self.isEnd = False  # Flag to represent end of a word.

class Solution:
    def __init__(self):
        self.root = TrieNode()
        # ToDo: Write Your Code Here.
        pass



    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        # ToDo: Write Your Code Here.
        node = self.root
        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
        pass

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        # ToDo: Write Your Code Here.
        node = self.root
        for char in word:
            if not char in node.children:
                return False
            node = node.children[char]
        return node.isEnd

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        # ToDo: Write Your Code Here.
        node = self.root
        for char in prefix:
            if not char in node.children:
                return False
            node = node.children[char]
        return True

