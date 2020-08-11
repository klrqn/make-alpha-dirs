#! python3 
# make a set of alphabetic directories import string

from pathlib import Path
import string

alphabet_string = string.ascii_uppercase

for letter in alphabet_string:
    p = Path("temp/{0}".format(letter))
    p.mkdir(parents=True, exist_ok=True)



