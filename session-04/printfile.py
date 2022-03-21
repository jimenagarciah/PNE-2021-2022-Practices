from pathlib import Path

# -- Constant with the new of the file to open
filename = input("File's name:") # Para que te imprima el file que le pidas

# -- Open and read the file
try:
    file_contents = Path(filename).read_text()
    # -- Print the contents on the console
    print(file_contents)
except FileNotFoundError:
    print("[ERROR]: FILE", filename, "not found")

