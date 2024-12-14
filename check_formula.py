import re
import os

RELA_PATH = "."  # Path of the file
FILE_NAME_A = "compareA.txt"  # Name of the file A
FILE_NAME_B = "compareB.txt"  # Name of the file B
FILE_WRITE = "convert_cn.txt"


def read_file(path):
    """
    read the file into a string
    """
    with open(path, "r", encoding="utf-8") as f:
        input_ = f.read()
    return input_


def find_formula(text):
    # Match inline LaTeX regex
    inline_pattern = r"\\\(.*?\\\)"
    # Match standalone LaTeX regex
    standalone_pattern = r"\\\[.*?\\\]"

    inline_matches = re.findall(inline_pattern, text)
    standalone_matches = re.findall(standalone_pattern, text)

    return inline_matches, standalone_matches


def match_formula(_fa, _fb, prefix):
    in_B_not_in_A = 0
    in_A_not_in_B = 0
    tmpb = []

    for item in _fb:
        if item in _fa:
            _fa.remove(item)
        else:
            tmpb.append(item)
            continue

    if len(tmpb):
        in_B_not_in_A = 1
        if prefix == "Standalone":
            print(
                "\n------------- [Standalone Formulas in B but not in A:",
                len(tmpb),
                "个] -------------",
            )
        else:
            print(
                "------------- [Inline Formulas in B but not in A:",
                len(tmpb),
                "个] -------------",
            )
    for i in tmpb:
        print(i)

    if len(_fa):
        in_A_not_in_B = 1
        print(
            "------------- [",
            prefix,
            "Formulas in A but not in B:",
            len(_fa),
            "个] -------------",
        )
        for item in _fa:
            print(item)

    if in_B_not_in_A + in_A_not_in_B == 0:
        print("--- No", prefix, " formula difference detected! ---")


def conv_into_jupyter_friendly(in_fb, st_fb):
    clt = []
    for c in in_fb:
        a = c.replace(r"\(", r"$")
        a = a.replace(r"\)", r"$")
        clt.append(a)
    for c in st_fb:
        a = c.replace(r"\[", r"$$")
        a = a.replace(r"\]", r"$$")
        clt.append(a)

    with open(os.path.join(RELA_PATH, FILE_WRITE), "w", encoding="utf-16") as f:
        for i in clt:
            f.write(i + "\n\n")


if __name__ == "__main__":
    text_A = read_file(os.path.join(RELA_PATH, FILE_NAME_A))
    text_B = read_file(os.path.join(RELA_PATH, FILE_NAME_B))

    text_A = re.sub(r"\n+", "", text_A).strip()
    text_B = re.sub(r"\n+", "", text_B).strip()

    inline_fa, standalone_fa = find_formula(text_A)
    inline_fb, standalone_fb = find_formula(text_B)

    conv_into_jupyter_friendly(inline_fb, standalone_fb)

    match_formula(inline_fa, inline_fb, "Inline")
    match_formula(standalone_fa, standalone_fb, "Standalone")
