import unittest

from estimate_sol import assembly_extractor

class TestAssemblyExtractor(unittest.TestCase):

    def test_extract_assembly_normal_usage(self):
        main_code, assembly_parts = assembly_extractor.extract_assembly("""\
blah;
assembly "something" (something else) 
{ assembly 
  {even inside curly brackets}
}
more non-assembly {even with brackets}
and assembly-non-things;
assembly {
    more assembly code
}
and something in the end"""
        )
        self.assertEqual("""\
blah;
assembly "something" (something else) 
{ASSEMBLY0}
more non-assembly {even with brackets}
and assembly-non-things;
assembly {ASSEMBLY1}
and something in the end""", 
        main_code)

        self.assertTupleEqual((
            """\
 assembly 
  {even inside curly brackets}
""",
            """\

    more assembly code
"""
        ), assembly_parts)

    def test_open_ended_assembly(self):
        main_code, assembly_parts = assembly_extractor.extract_assembly(
            ";assembly {no ending curly bracket"
        )

        self.assertEqual(";assembly {ASSEMBLY0", main_code)
        self.assertTupleEqual(
            ("no ending curly bracket",),
            assembly_parts
        )