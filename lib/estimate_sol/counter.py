from collections import namedtuple
from .comment_remover import remove_comments
from .import_extractor import extract_imports
from .import_resolver import resolve_import
from .string_blanker import blank_strings
from .assembly_extractor import extract_assembly

CountingResult = namedtuple("CountingResult", "files deps unresolved_deps missing_files".split(" "))

def count_code_lines(src):
    return len([l for l in src.split("\n") if l.strip()])

PUNCTUATIONS = set(r"~!%^&*()-=+[{]}|;:\"'<,>.?/")

def count_punctuations(src):
    rv = 0

    for c in src: 
        if c in PUNCTUATIONS:
            rv+=1

    return rv

def count_with_deps(files, encoding, assembly_multiplier, counter_fun):
    files = {f.resolve() for f in files}
    files_to_analyze = {*files} # start with files to count, no dependencies

    item_counts = {}
    unresolved_deps = set()
    missing_files = set()

    while files_to_analyze:
        f = files_to_analyze.pop()
        if not f.exists():
            missing_files.add(f)
            continue

        src = remove_comments(f.read_text(encoding))
        solidity_part, assembly_parts = extract_assembly(blank_strings(src))
        item_counts[f] = counter_fun(solidity_part)
        for p in assembly_parts:
            item_counts[f] += counter_fun(p) * assembly_multiplier

        imps = extract_imports(src)
        for imp in imps:
            resolved_imp = resolve_import(imp, f)
            if not resolved_imp:
                unresolved_deps.add(imp)
                continue

            resolved_imp = resolved_imp.resolve()

            if resolved_imp in item_counts:
                continue
            if resolved_imp in missing_files:
                continue
            if resolved_imp in files_to_analyze:
                continue

            files_to_analyze.add(resolved_imp)

    return CountingResult(
        files={k: v for k, v in item_counts.items() if k in files},
        deps={k: v for k, v in item_counts.items() if k not in files},
        unresolved_deps=unresolved_deps,
        missing_files=missing_files
    )
