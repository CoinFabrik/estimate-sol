#!/usr/bin/env python3
import sys
import argparse
import pathlib
import os

from . import counter
from . import __VERSION__

def getenv_with_default(key, default): 
    rv = os.getenv(key)
    if rv is None:
        return default
    return rv

COUNT_MODES = {
    "lines": {
        "count_fun": counter.count_code_lines,
        "default_week_size": float(getenv_with_default("ESTIMATE_SOL_DEFAULT_LINES_PER_WEEK", "1"))
    },
    "punct": {
        "count_fun": counter.count_punctuations,
        "default_week_size": float(getenv_with_default("ESTIMATE_SOL_DEFAULT_PUNCTUATIONS_PER_WEEK", "1"))
    }
}

def argparser():
    parser = argparse.ArgumentParser(description="Estimate solidity audit sizes.")
    parser.add_argument("files", nargs="+", help="Files to be audited.", type=pathlib.Path)
    parser.add_argument(
        "--punctuations", 
        "-p", 
        action="store_const",
        dest="count_mode", 
        const="punct", 
        default="lines", 
        help="Use punctuations for counting (default: lines)"
    )
    parser.add_argument("--encoding", "-e", default="utf-8", help="File encoding (default=%(default)s).")
    parser.add_argument(
        "--dependencies-multiplier", 
        "-d", 
        default=float(getenv_with_default("ESTIMATE_SOL_DEFAULT_DEPENDENCIES_MULTIPLIER", "1")),
        type=float,
        help="Multiplier to estimate non-audited dependencies (default=%(default)s)."
    )
    parser.add_argument(
        "--assembly-multiplier",
        default=float(getenv_with_default("ESTIMATE_SOL_DEFAULT_ASSEMBLY_MULTIPLIER", "1")),
        type=float,
        help="Multiplier to estimate assembly code (default=%(default)s)."
    )
    parser.add_argument(
        "--week-size",
        "-w",
        type=float,
        help="Number of items to audit per week. Defaults: (" + ", ".join(f"{k}:{v['default_week_size']}" for k,v in COUNT_MODES.items()) + ")"
    )
    parser.add_argument(
        "-a",
        "--absolute_paths",
        action="store_true",
        help="Show all paths as absolute (by default relative paths are shown if inside current directory)."
    )
    parser.add_argument("-V", "--version", action="version", version="%(prog)s " + __VERSION__)

    return parser

CURRENT_PATH = pathlib.Path('.').resolve()
def relativize(path):
    try:
        return path.relative_to(CURRENT_PATH)
    except ValueError:
        return path

def print_count_result(
    *, 
    count_result, 
    week_size, 
    dependencies_multiplier,
    absolute_paths
):
    path_transformation = (lambda x:x) if absolute_paths else relativize

    print("Files to audit")
    if count_result.files:
        for k,v in sorted(count_result.files.items(), key=lambda e:e[0]):
            print(f"\t{path_transformation(k)} ({v})")
    else:
        print("\tNo audited files")
    
    print("Dependencies")
    if count_result.deps:
        for k,v in sorted(count_result.deps.items(), key=lambda e:e[0]):
            print(f"\t{path_transformation(k)} ({v})")
    else:
        print("\tNo dependencies found")
    
    print("Unresolved deps")
    if count_result.unresolved_deps:
        for d in sorted(count_result.unresolved_deps):
            print(f"\t{d}")
    else:
        print("\tNo unresolved deps")
    
    print("Missing files")
    if count_result.missing_files:
        for f in sorted(count_result.missing_files):
            print(f"\t{path_transformation(f)}")
    else:
        print("\tNo missing files")

    item_count_files = sum(count_result.files.values())
    item_count_deps = sum(count_result.deps.values())
    print("Total item counts")
    print(f"\tfiles: {item_count_files}")
    print(f"\tdeps: {item_count_deps}")
    
    print(f"Estimated effort: {(item_count_files + item_count_deps * dependencies_multiplier)/week_size}")

def main(argv):
    args = argparser().parse_args(argv[1:])
    count_result = counter.count_with_deps(args.files, args.encoding, args.assembly_multiplier, COUNT_MODES[args.count_mode]["count_fun"])
    print_count_result(
        count_result=count_result, 
        week_size=args.week_size or COUNT_MODES[args.count_mode]["default_week_size"], 
        dependencies_multiplier=args.dependencies_multiplier,
        absolute_paths=args.absolute_paths,
    )

def run():
    main(sys.argv)

if __name__ == '__main__':
    run()
