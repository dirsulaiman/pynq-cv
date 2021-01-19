#! python3 extract-from-top-result.py "fpga-aveblur"
#! top -b -p PID >> fpga-aveblur1.txt

import sys
import re

file_name = sys.argv[1]

def replace_whitespace(text):
    text = re.sub( r"[\s]{2,}", " ",text)
    text = re.sub( r"[\t ]", '; ', text)
    return re.sub( r"[\n]", ';\n', text)

def clean_file(file_input, file_name):
    file_cleaned = open(f"performance-test/cleared_whitespace/{file_name}.txt", "w")
    s = ""
    for i in file_input:
        s = s+i
    s = re.sub(r'\n[\s\n]+', "\n", s)
    file_cleaned.seek(0)
    file_cleaned.write(s)
    file_cleaned.close()


def extract (file_name, percobaan):
    index = 0
    posisi = 7

    file = open(f"performance-test/{file_name}{percobaan}.txt")
    clean_file(file, file_name+str(percobaan))

    file_input = open(f"performance-test/cleared_whitespace/{file_name+str(percobaan)}.txt", "r")
    file_output = open(f"performance-test/csv/{file_name}{percobaan}.csv", "w")

    for line in file_input:
        index = index + 1
        if (index == 6):
            # print(replace_whitespace(line))
            file_output.write(replace_whitespace(line))

        if (index == posisi):
            # print(replace_whitespace(line))
            file_output.write(replace_whitespace(line))
            posisi = posisi + 7

    file_input.close()
    file_output.close()


for i in range(1, 6):
    extract(file_name, i)