import unittest

from solution import solution

class TestSolution(unittest.TestCase):

    def test_empty_input(self):
        print("\n", "testing solution:")
        self.assertEqual(solution([]), None)
        print("\n","1) solution doesn't compute if input is missing")
   
    def test_solution_is_correct(self):
        with open("output.txt", 'r') as f:
            output = f.read()
        self.assertEqual(solution(["inputs/comma.txt", "inputs/pipe.txt", "inputs/space.txt"]), output)
        print("\n","2) the generated output is correct")


unittest.main()