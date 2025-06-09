from dynamic_programming.subsequence.distinct_subsequence import distinct_subsequence
import unittest


class TestDistinctSubsequence(unittest.TestCase):
    def test_example(self):
        self.assertEqual(distinct_subsequence("rabbbit", "rabbit"), 3)

    def test_empty_t(self):
        self.assertEqual(distinct_subsequence("abc", ""), 1)

    def test_empty_s(self):
        self.assertEqual(distinct_subsequence("", "abc"), 0)

    def test_s_shorter_than_t(self):
        self.assertEqual(distinct_subsequence("ab", "abc"), 0)

    def test_no_subsequence(self):
        self.assertEqual(distinct_subsequence("abc", "def"), 0)

    def test_single_char_match(self):
        self.assertEqual(distinct_subsequence("aaa", "a"), 3)

    def test_single_char_no_match(self):
        self.assertEqual(distinct_subsequence("abc", "d"), 0)


if __name__ == "__main__":
    unittest.main()
