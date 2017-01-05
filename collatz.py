import unittest
import time


class Collatz:

    def __init__(self):
        self.memory = {}

    def _collatz(self, number):
        return number/2 if number % 2 == 0 else (3 * number) + 1

    def _get_size_of_collatz_vector(self, number):
        value = 1
        collatz_number = number

        while collatz_number != 1:
            if self.memory.has_key(collatz_number):
                value += self.memory[collatz_number]
                break

            collatz_number = self._collatz(collatz_number)
            value += 1

        self.memory[number] = value

        return value

    def find_integer_with_bigger_collatz_sequence(self):
        max_value = 0
        max_length = 0
        self.memory = {}

        for number in range(1, 1000000):
            length = self._get_size_of_collatz_vector(number)

            if length > max_length:
                max_length = length
                max_value = number

        return max_value

class TestCollatz(unittest.TestCase):

    def setUp(self):
        self.collatz = Collatz()

    def test_algorithm_efficiency(self):
        start_time = time.time()
        self.collatz.find_integer_with_bigger_collatz_sequence()
        end_time = time.time() - start_time

        print ("Time: {}".format(end_time))

        self.assertTrue(end_time < 5)

    def test_find_integer_with_bigger_sequence(self):
        self.assertEqual(self.collatz.find_integer_with_bigger_collatz_sequence(), 837799)

if __name__ == '__main__':
    unittest.main()