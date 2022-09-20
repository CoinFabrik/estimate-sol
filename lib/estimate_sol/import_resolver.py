from pathlib import Path

def resolve_import(path, parent_file):
    if "." != path[0]:
        return None
    return Path(parent_file).parent / path