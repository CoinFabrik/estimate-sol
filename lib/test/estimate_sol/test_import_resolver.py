import unittest
from pathlib import Path

from estimate_sol.import_resolver import resolve_import

class TestImportResolver(unittest.TestCase):

    def test_import_resolution(self):
        for path, parent_file, expected_resolution in (
            ("@something", "/foo/bar/baz.sol", None),
            ("aaa", "/foo/bar/baz.sol", None),
            ("./a/b.sol", "/foo/bar/baz.sol", "/foo/bar/a/b.sol"),
            ("../a/b.sol", "/foo/bar/baz.sol", "/foo/bar/../a/b.sol")
        ):
            resolved_path = resolve_import(path, parent_file)
            if expected_resolution is None:
                self.assertIsNone(resolved_path, f"Resolved path for {path=} {parent_file=} but it should not")
            else:
                self.assertEqual(
                    Path(expected_resolution).resolve(), 
                    Path(resolved_path).resolve(),
                    f"Wrong path resolution for {path=} {parent_file=}"
                )