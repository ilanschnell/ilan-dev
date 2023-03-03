import unittest

from ilan_dev import lcp, human_bytes, get_dirs


class Tests(unittest.TestCase):

    def test_lcp(self):
        self.assertTrue(lcp([]) is None)

        for lst, res in [
                (['banana'],                 'banana'),
                (['', 'pinetree'],           ''),
                (['pineapple', 'pinetree'],  'pine'),
                (['apple', 'banana'],        ''),
        ]:
            self.assertEqual(lcp(lst), res)

    def test_human_bytes(self):
        for n, res in [
                (0,        '0'),
                (1023,     '1023'),
                (1024,     '1K'),
                (1 << 20,  '1.0M'),
                (1 << 30,  '1.00G'),
        ]:
            self.assertEqual(human_bytes(n), res)

class GetDirsTests(unittest.TestCase):

    lst = [(path, 'file' not in path) for path in [
        'a',
        'a/file',
        'b',
        'b/c',
        'b/c/d',
        'b/c/e',
        'b/file',
        'c',
        'd/e/file',
        ]]

    def test_empty(self):
        self.assertEqual(get_dirs([], 'empty'), set())

        self.assertEqual(get_dirs(self.lst),  # default mode empty
                         set(['b/c', 'b/c/d', 'b/c/e', 'c']))

    def test_missing(self):
        self.assertEqual(get_dirs([], 'missing'), set())

        self.assertEqual(get_dirs(self.lst, 'missing'),
                         set(['d', 'd/e']))


if __name__ == '__main__':
    unittest.main()
