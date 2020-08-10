#! python3
# make a set of alphabetic directories

import string
import os
from pathlib import Path

currentDir = Path.cwd()
print(currentDir)

# make a list of the alphabet
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

# for letter in alphabet_list:
#    print(alphabet_list)

print(alphabet_list)

