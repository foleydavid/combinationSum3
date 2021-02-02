# TESTING PUSH PULL PYCHARM 2

import unittest
from Solution import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_combinationSum3(self):
        self.assertEqual(self.sol.combinationSum3(3, 7), [[1, 2, 4]])
        self.assertEqual(self.sol.combinationSum3(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
        self.assertEqual(self.sol.combinationSum3(4, 1), [])
        self.assertEqual(self.sol.combinationSum3(3, 2), [])
        self.assertEqual(self.sol.combinationSum3(9, 45), [[1, 2, 3, 4, 5, 6, 7, 8, 9]])

        ans = [[1, 2, 9], [1, 3, 8], [1, 4, 7], [1, 5, 6], [2, 3, 7], [2, 4, 6], [3, 4, 5]]
        self.assertEqual(self.sol.combinationSum3(3, 12), ans)

if __name__ == "__main__":
    unittest.main()
