import unittest


def insertion_sort(a):
    for i, v in enumerate(a):
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            a[j] = v
            j = j - 1


def insertion_sort_desc(a):
    for i, v in enumerate(a):
        j = i - 1
        while j >= 0 and a[j] < v:
            a[j + 1] = a[j]
            a[j] = v
            j = j - 1


class TestInsertSort(unittest.TestCase):
    def test_insert_sort(self):
        l = [10, 3, 20, 49, 3, 4]
        insertion_sort(l)
        self.assertEqual(l, [3, 3, 4, 10, 20, 49])

    # task 2.1.2
    def test_insertion_sort_desc(self):
        l = [31, 41, 59, 26, 41, 58]
        insertion_sort_desc(l)
        self.assertEqual(l, [59, 58, 41, 41, 31, 26])


if __name__ == '__main__':
    unittest.main()
