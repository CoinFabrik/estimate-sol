import unittest

from estimate_sol import counter

class TestCounter(unittest.TestCase):

    def test_count_code_lines(self):
        self.assertEqual(
            2,
            counter.count_code_lines("\n\n1;\n\n2;\n\n")
        )

    def test_count_punctuations(self):
        all_punctuations = "".join(counter.PUNCTUATIONS)

        self.assertEqual(
            len(all_punctuations),
            counter.count_punctuations("a" + all_punctuations + "b")
        )