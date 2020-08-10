#! python3 
# make a set of alphabetic directories import string

import os
from pathlib import Path
import string

currentDir = Path.cwd()
print(currentDir)

# make a list of the alphabet
alphabet_string = string.ascii_uppercase
# alphabet_string = "ABCDEFG...WXYZ" 
alphabet_list = list(alphabet_string)
# alphabet_list = ['A', 'B' ... 'Y', 'Z']
# think transitioning from str to list isn't needed

for letter in alphabet_list:
    p = Path("temp/{0}".format(letter))
    print(p)
    p.mkdir(parents=True, exist_ok=True)


