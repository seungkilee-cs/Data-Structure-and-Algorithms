class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # set the first char as initial node, and iterated until the word is completed
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # set the last node as word and is_end to true
        node.word = word
        node.is_end = True

    def search(self, word: str) -> bool:
        # create dummy node
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # return if the last char is the end of the word
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
