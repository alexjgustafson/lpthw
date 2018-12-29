from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()
open(to_file, 'w').write(indata)

print(f"Copied from {from_file} to {to_file}")