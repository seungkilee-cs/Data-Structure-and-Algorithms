import unittest
from tree.trie.trie import Trie


class TestTrie(unittest.TestCase):
    trie = Trie()
    trie.insert("apple")
    print("apple inserted")
    print("search for 'apple' -> True")
    assert trie.search("apple"), "apple should be found"
    print("search for 'app' -> False")
    assert not trie.search("app"), "app is a prefix, not a word"
    print("startswith 'app' -> True")
    assert trie.startsWith("app"), "app is a prefix"
    trie.insert("app")
    print("app inserted")
    print("search for 'app' -> True")
    assert trie.search("app"), "app should now be found"
    trie.insert("banana")
    print("banana inserted")
    print("search for 'banana' -> True")
    assert trie.search("banana")
    print("search for 'ban' -> True")
    assert trie.startsWith("ban")
    print("startswith for 'band' -> False")
    assert not trie.startsWith("band")
    print("All Trie tests passed!")


if __name__ == "__main__":
    unittest.main()
