import unittest


def insert_sort(a):
    for i, v in enumerate(a):
        j = i - 1
        while j > 0 and a[j] > v:
            a[j + 1] = a[j]
            a[j] = v
            j = j - 1


class TestInsertSort(unittest.TestCase):
    def test_insert_sort(self):
        l = [1, 3, 20, 49, 3, 4]
        insert_sort(l)
        self.assertEqual(l, [1, 3, 3, 4, 20, 49])


if __name__ == '__main__':
    unittest.main()
