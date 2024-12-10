import re
import os

RELA_PATH = "."  # Path of the file
FILE_NAME_A = "compareA.txt"  # Name of the file A
FILE_NAME_B = "compareB.txt"  # Name of the file B



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

def match_inline_formula(in_fa, in_fb):

    for item in in_fb:
        if item in in_fa:
            in_fa.remove(item)
        else:
            print(item, "in B can't be found in A!")
            continue

    if len(in_fa):
        for item in in_fa:
            print(item, "in A but can't be found in B!")

def match_standalone_formula(st_fa, st_fb):

    for item in st_fb:
        if item in st_fa:
            st_fa.remove(item)
        else:
            print(item, "in B can't be found in A!")
            continue

    if len(st_fa):
        for item in st_fa:
            print(item, "in A but can't be found in B!")

if __name__ == "__main__":

    text_A = read_file(os.path.join(RELA_PATH, FILE_NAME_A))
    text_B = read_file(os.path.join(RELA_PATH, FILE_NAME_B))

    text_A = re.sub(r"\n+", "", text_A).strip()
    text_B = re.sub(r"\n+", "", text_B).strip()


    inline_fa, standalone_fa = find_formula(text_A)
    inline_fb, standalone_fb = find_formula(text_B)

    match_inline_formula(inline_fa, inline_fb)
    match_standalone_formula(standalone_fa, standalone_fb)