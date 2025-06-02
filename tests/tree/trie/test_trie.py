import unittest
from tree.trie.trie import Trie


def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True, "apple should be found"
    assert trie.search("app") == False, "app is a prefix, not a word"
    assert trie.startsWith("app") == True, "app is a prefix"
    trie.insert("app")
    assert trie.search("app") == True, "app should now be found"
    trie.insert("banana")
    assert trie.search("banana") == True
    assert trie.startsWith("ban") == True
    assert trie.startsWith("bana") == True
    assert trie.startsWith("band") == False
    print("All Trie tests passed!")
