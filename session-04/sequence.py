from pathlib import Path
filename = input("File's name:")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    total = 0
    for line in body:
        total = total + len(line)
    print("Total number of bases:", total)
except FileNotFoundError:
    print("[ERROR]: FILE", filename, "not found")
except IndexError:
    print("[ERROR]: FILE", filename, "is empty")
