import unittest

from estimate_sol.comment_remover import remove_comments

class TestSolidityCommentRemover(unittest.TestCase):

    def test_comment_removal(self):
        for original, expected_removed in (
            ('a', 'a'),

            # # Single line comments
            ('a/b\ncd', 'a/b\ncd'),
            ('ab//cd\nef', 'ab\nef'),

            # # Multiline comments
            ('ab/*cd*/ef', 'abef'),
            ('a/b*/*c*d/**/*e/f', 'a/b**e/f'),

            # Strings
            ('ab"\\"c//"//ignored\nde', 'ab"\\"c//"\nde'),
            ("ab'\\'c//'//ignored\nde", "ab'\\'c//'\nde"),
        ):
            self.assertEqual(expected_removed, remove_comments(original), f"Cannot remove comments for {original=!r}")
