import re

ASSEMBLY_START_RE = re.compile(r"[};]\s*assembly([\s(][^{]*)?\{")

def extract_assembly(src):
    main_code = ""
    assembly_parts = []
    last_pos = 0
    while True:
        match = ASSEMBLY_START_RE.search(src, last_pos)
        if not match:
            break
        main_code += src[last_pos:match.end()]
        main_code += f"ASSEMBLY{len(assembly_parts)}"
        assembly_start = match.end()
        last_pos = assembly_start

        curly_bracket_count = 1
        while last_pos < len(src):
            if src[last_pos] == "{":
                curly_bracket_count += 1
            elif src[last_pos] == "}":
                curly_bracket_count -= 1
            if curly_bracket_count == 0:
                break
            last_pos +=1

        assembly_parts.append(src[assembly_start:last_pos])

    main_code += src[last_pos:]
    
    return main_code, tuple(assembly_parts)