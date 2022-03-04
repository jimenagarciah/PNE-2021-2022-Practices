from pathlib import Path
file = "RNU6_269P.txt"
text = Path(file).read_text()
print("First line of the RNU6_269P.txt file:")
print(text[:text.find("\n")])