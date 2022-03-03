list_genes = ["U5", "FRAT1", "ADA"]
for l in list_genes:
    print(len(Seq0.seq_read_fasta("./sequences/" + l + ".txt")))