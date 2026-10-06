import unittest
from solution import group_anagrams

class TestGroupAnagrams(unittest.TestCase):
    def test_grouping(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res = [sorted(g) for g in group_anagrams(words)]
        res.sort()
        expected = [sorted(["bat"]), sorted(["nat", "tan"]), sorted(["ate", "eat", "tea"])]
        expected.sort()
        self.assertEqual(res, expected)

    def test_single_and_empty(self):
        self.assertEqual(group_anagrams([""]), [[""]])
        self.assertEqual(group_anagrams(["a"]), [["a"]])

if __name__ == "__main__":
    unittest.main()
