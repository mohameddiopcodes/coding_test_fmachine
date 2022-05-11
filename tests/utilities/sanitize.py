import unittest

from utilities.open_file import open_file
from utilities.sanitize import sanitize

correct_output = [['Abercrombie Neil Male 2/13/1943 Tan', 'Bishop Timothy Male 4/23/1967 Yellow', 'Kelly Sue Male 7/12/1959 Pink'], ['Smith Steve Male 3/3/1985 Red', 'Bonk Radek Male 6/3/1975 Green', 'Bouillon Francis Male 6/3/1975 Blue'], ['Kournikova Anna Female 6/3/1975 Red', 'Hingis Martina Female 4/2/1979 Green', 'Seles Monica Female 12/2/1973 Black']]

class TestSplitValuesFunction(unittest.TestCase):

    def test_split_value_outputs_correct_values(self):
        print("\n", "testing utilities/sanitize:")
        input_files = ["inputs/comma.txt", "inputs/pipe.txt", "inputs/space.txt"]
        result = []

        for file in input_files:
            result.append(sanitize(open_file(file)))
        self.assertEqual(result, correct_output)

        print("\n", "2) sanitizes correctly")

unittest.main()
