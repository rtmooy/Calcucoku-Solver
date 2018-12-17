import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
      
   def test_check_rows0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_rows_valid(puzzle))
   
   def test_check_rows1(self):
      puzzle = []
      puzzle.append([1, 1, 1, 1, 1])
      puzzle.append([6, 6, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 1, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_rows_valid(puzzle))
  
   def test_check_columns0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertTrue(check_columns_valid(puzzle))

   def test_check_columns1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([1, 6, 2, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_columns_valid(puzzle))

   def test_check_columns2(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([3, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([1, 6, 1, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      self.assertFalse(check_columns_valid(puzzle))

   def test_check_cages0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 4, 1])
      cages.append([5, 2, 1, 8])
      self.assertTrue(check_cages_valid(puzzle, cages))

   def test_check_cages1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 2, 5])
      cages.append([7, 3, 2, 6, 7])
      cages.append([9, 2, 4, 9])
      self.assertFalse(check_cages_valid(puzzle, cages))

   def test_check_cages1(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 1, 2, 3])
      cages.append([9, 2, 1, 8])
      self.assertFalse(check_cages_valid(puzzle, cages))

   def test_check_cages2(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 1, 2, 4])
      cages.append([9, 2, 0, 9])
      self.assertFalse(check_cages_valid(puzzle, cages))

   def test_check_valid0(self):
      puzzle = []
      puzzle.append([5, 1, 2, 3, 4])
      puzzle.append([1, 2, 3, 4, 5])
      puzzle.append([2, 3, 0, 5, 1])
      puzzle.append([3, 0, 0, 1, 2])
      puzzle.append([0, 0, 0, 0, 0])
      cages = []
      cages.append([6, 2, 0, 5])
      cages.append([7, 3, 2, 4, 1])
      cages.append([5, 2, 1, 8])
      self.assertTrue(check_cages_valid(puzzle, cages))



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

