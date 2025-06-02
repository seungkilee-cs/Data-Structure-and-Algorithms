class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word: str) -> bool:
        return False

    def startsWith(self, char: str) -> bool:
        return False
