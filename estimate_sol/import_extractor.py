import re

SYMBOL_REGEX_PART = r"([a-zA-Z$_][a-zA-Z0-9$_]*)"
AS_REGEX_PART = r"(\s*as\s+" + SYMBOL_REGEX_PART + ")?"
PATH_MATCH_DOUBLE_QUOTES = r"(\"(?P<path>[^\"]*)\")"
PATH_MATCH_SINGLE_QUOTES = r"(\'(?P<path>[^\']*)\')"
SYMBOL_ALIASES = r"(\s*\{[^}]*\})"

EXTRACT_REGEXES = []
for path_match in (
    PATH_MATCH_DOUBLE_QUOTES, 
    PATH_MATCH_SINGLE_QUOTES,
):
    for r in (
        r"import\s+" + path_match + r"\s*" + AS_REGEX_PART, # simple import
        r"import" + SYMBOL_ALIASES + r"\s*from\s*" + path_match, # import {aliases} from
        r"import\s*\*\s*as\s+" + SYMBOL_REGEX_PART + r"\s+from\s*" + path_match, # import * as blah from
    ):
        EXTRACT_REGEXES.append(re.compile(r";\s*"+r+r"\s*;", re.MULTILINE))


def extract_imports(code):
    code = code.replace("\r", "") # Windows compatibility hack
    rv = set()

    for r in EXTRACT_REGEXES:
        code2 = code
        while True:
            m = r.search(code2)
            if not m:
                break
            rv.add(m.group("path"))
            code2 = code2[m.end()-1:] #-1 to keep trailing ; for next match

    return rv
