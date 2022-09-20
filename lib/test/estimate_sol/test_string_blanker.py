import unittest

from estimate_sol import string_blanker

class TestStringBlanker(unittest.TestCase):

    def test_blank_strings(self):

        self.assertEqual(
            "a''d\"\"g",
            string_blanker.blank_strings("a'b\\'c\\\"'d\"e\\\"\\'f\"g")
        )