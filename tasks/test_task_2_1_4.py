import unittest

import tasks.task_2_1_4


class TestBitSum(unittest.TestCase):
    def test_bit_sum(self):
        self.assertEqual(tasks.task_2_1_4.bit_sum([1, 1, 1, 1], [1, 1, 1, 1]), [1, 1, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
