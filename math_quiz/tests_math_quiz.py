import unittest
from math_quiz import genrate_random_int, genrate_random_operation, generate_problem


class TestMathGame(unittest.TestCase):

    def test_genrate_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = genrate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_genrate_random_operation(self):
        # Test if random operations generated are valid
        for _ in range(1000):  # Test a large number of random values
            rand_op = genrate_random_operation()
            self.assertTrue(rand_op in ['+', '-', '*'])

    def test_generate_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '*', '5 * 2', 10),
                (8, 3, '+', '8 + 3', 11),
                (2, 1, '-', '2 - 1', 1),
                (10, 5, '*', '10 * 5', 50),
                (7, 4, '+', '7 + 4', 11),
                (3, 2, '-', '3 - 2', 1),
                (9, 6, '*', '9 * 6', 54),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
