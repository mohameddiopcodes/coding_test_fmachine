import unittest

from utilities.open_file import open_file

correct_output = [['Abercrombie, Neil, Male, Tan, 2/13/1943', 'Bishop, Timothy, Male, Yellow, 4/23/1967', 'Kelly, Sue, Female, Pink, 7/12/1959'], ['Smith | Steve | D | M | Red | 3-3-1985', 'Bonk | Radek | S | M | Green | 6-3-1975', 'Bouillon | Francis | G | M | Blue | 6-3-1975'], ['Kournikova Anna F F 6-3-1975 Red', 'Hingis Martina M F 4-2-1979 Green', 'Seles Monica H F 12-2-1973 Black']]

class TestOpenFileFunction(unittest.TestCase):

    def test_open_file_outputs_correct_values(self):
        print("\n", "testing utilities/open_file:")
        input_files = ["inputs/comma.txt", "inputs/pipe.txt", "inputs/space.txt"]
        result = []

        for file in input_files:
            result.append(open_file(file))
        self.assertEqual(result, correct_output)
        
        print("\n", "1) opens files correctly")

unittest.main()