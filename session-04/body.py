from pathlib import Path
filename = input("File's name:")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    print("Body of the", filename, "file:")
    for line in body:
        print(line)
except FileNotFoundError:
    print("[ERROR]: FILE", filename, "not found")
except IndexError:
    print("[ERROR]: FILE", filename, "is empty")
