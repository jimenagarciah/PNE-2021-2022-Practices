elif command == "LEN":
    if len(slices) == 1:
        sequence = Seq()
    else:
        bases = slices[1]
        sequence = Seq(bases)

    response = f"{sequence.len()}\n"