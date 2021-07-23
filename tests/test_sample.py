"""sample.pyのテストモジュール
"""

import unittest
import numpy as np
import sandbox.sample as sample

class SampleTest(unittest.TestCase):
    def test_mult_normal(self):
        """通常の行列積ができることを確認する．
        """
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[4, 3], [2, 1]])
        c = sample.mult(a, b)
        expect = np.array([[8, 5], [20, 13]])
        eps = 1.0e-10
        self.assertTrue(np.linalg.norm(c - expect) < eps)

    def test_mult_one(self):
        """1つの行列が与えられたとき，そのまま返されることを確認する．
        """
        a = np.array([[1, 2], [3, 4]])
        c = sample.mult(a)
        expect = a
        eps = 1.0e-10
        self.assertTrue(np.linalg.norm(c - expect) < eps)

    def test_mult_three_mats(self):
        """3つの行列積が計算できることを確認する．
        """
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[4, 3], [2, 1]])
        c = np.array([[2, -1], [-1, 2]])
        d = sample.mult(a, b, c)
        expect = np.array([[11, 2], [27, 6]])
        eps = 1.0e-10
        self.assertTrue(np.linalg.norm(d - expect) < eps)


if __name__ == '__main__':
    unittest.main()

