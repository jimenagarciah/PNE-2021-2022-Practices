BASES = ["A", "C", "T", "G"]

def seq_ping():
    print("Ok")

def seq_read_fasta(filename):
    from pathlib import Path

    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:] #list[str]
    sequence = ""
    for line in body:
        sequence += line
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq: str, base):
    return seq.count(base)

def seq_count(seq):
    d = {}
    for base in BASES:
        d[base] = seq_count_base(seq, base)
    return d

