import re
import os

RELA_PATH = "."  # Path of the file
FILE_NAME_C = "response.txt"  # Name of the file A
FILE_WRITE = "convert_rp.txt"


def read_file(path):
    """
    read the file into a string
    """
    with open(path, "r", encoding="utf-8") as f:
        input_ = f.read()
    return input_


def replace_formula(text):
    # Match inline LaTeX regex
    inline_pattern = r"\\\(.*?\\\)"
    # Match standalone LaTeX regex
    standalone_pattern = r"\\\[.*?\\\]"
    standalone_pattern_multiline = r"\\\[(?:.|\n)*?\\\]"

    # Replace inline LaTeX with $...$
    inline_matches = re.findall(inline_pattern, text)
    # Replace standalone LaTeX with $$...$$
    standalone_matches = re.findall(standalone_pattern, text)
    # Replace multiline standalone LaTeX with $$...$$
    standalone_matches_multiline = re.findall(standalone_pattern_multiline, text)

    for inline_match in inline_matches:
        text = text.replace(inline_match, r"$" + inline_match[2:-2] + r"$")
    for standalone_match in standalone_matches:
        text = text.replace(standalone_match, r"$$" + standalone_match[2:-2] + r"$$")
    for standalone_match in standalone_matches_multiline:
        text = text.replace(standalone_match, r"$$" + standalone_match[3:-3] + r"$$")

    with open(os.path.join(RELA_PATH, FILE_WRITE), "w", encoding="utf-16") as f:
        f.write(text)


if __name__ == "__main__":
    text = read_file(os.path.join(RELA_PATH, FILE_NAME_C))
    replace_formula(text)
