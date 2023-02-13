from random import randint
import unittest
from MergeSort import merge_sort
from Insertion import insertion_sort
from Counting import counting_sort


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.ls = []
        for i in range(1000):
            self.ls.append(randint(1, 10000))

    def test_merge(self):
        self.assertEqual(sorted(self.ls), merge_sort(self.ls))

    def test_merge_reverse(self):
        self.assertEqual(sorted(self.ls, reverse=True), merge_sort(self.ls, reverse=True))

    def test_insertion(self):
        self.assertEqual(sorted(self.ls), insertion_sort(self.ls))

    def test_insertion_reverse(self):
        self.assertEqual(sorted(self.ls, reverse=True), insertion_sort(self.ls, reverse=True))

    def test_counting(self):
        ls = list(map(lambda a: a % 100, self.ls))[:20]
        self.assertEqual(sorted(ls), counting_sort(ls))

    def test_counting_reverse(self):
        ls = list(map(lambda a: a % 100, self.ls))[:20]
        self.assertEqual(sorted(ls, reverse=True), counting_sort(ls, reverse=True))


if __name__ == '__main__':
    unittest.main()
