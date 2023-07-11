import unittest
from helpers.sequences import init_sequence, Items


class SequenceTestCase(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(init_sequence("example")), Items)

    def test_values_str(self):
        self.assertEqual(type(init_sequence("example")[1:2]), list)


if __name__ == "__main__":
    unittest.main()
