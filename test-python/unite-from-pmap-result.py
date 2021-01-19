#! python3 unite-from-pmap-result.py "result-pmap"
#! sudo pmap PID | tail -n1 > result-pmapX.txt 

import sys
import re

def replace_whitespace(text):
    text = text[1:]
    text = re.sub( r"[\s]{2,}", " ",text)
    text = re.sub( r"[\t ]", '; ', text)
    return re.sub( r"[\n]", ';\n', text)

file_input = sys.argv[1]

file_1 = open(f"performance-test/{file_input}1.txt")
file_2 = open(f"performance-test/{file_input}2.txt")
file_3 = open(f"performance-test/{file_input}3.txt")
file_4 = open(f"performance-test/{file_input}4.txt")
file_5 = open(f"performance-test/{file_input}5.txt")

file_output = open(f"performance-test/csv/{file_input}-all.csv", "w")

file_output.write(replace_whitespace(file_1.readline()))
file_output.write(replace_whitespace(file_2.readline()))
file_output.write(replace_whitespace(file_3.readline()))
file_output.write(replace_whitespace(file_4.readline()))
file_output.write(replace_whitespace(file_5.readline()))

file_1.close()
file_2.close()
file_3.close()
file_4.close()
file_5.close()
file_output.close()