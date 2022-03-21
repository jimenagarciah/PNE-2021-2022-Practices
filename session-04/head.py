from pathlib import Path
filename = input("File's name:")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    head = lines[0]
    print("First line of the", filename, "file:", head)
except FileNotFoundError:
    print("[ERROR]: FILE", filename, "not found")
except IndexError:
    print("[ERROR]: FILE", filename, "is empty")


