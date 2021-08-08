import unittest
import calc


class testclass_calc(unittest.TestCase):
    def test_inputValidate(self):
        # Arrange
        testInput = "abcd"

        # Act
        testResult = calc.inputValidate(testInput)

        # Assert
        self.assertEqual(testResult, None)

        # print("Result of test_calculate is: "+testValidate)

    def test_calculate(self):
        # Arrange
        testInput1 = "20"
        testInput2 = "30"
        testInput3 = "1"

        # Act
        testResult = calc.calculate(testInput1, testInput2, testInput3)

        # Assert
        self.assertEqual(testResult, "\nResult is: 50\n")
        # print("Result of test_calculate is: "+ testValidate)


if __name__ == '__main__':
    unittest.main()
