interactions = "data/raw/Network_Interactions.csv"

with open(output_file, "W") as out: 
    out.write("TF\tTotal de genes\tActivados\tReprimidos\tTipo\tLista de genes\n")
    
    for line in f:
        line = line.strip()

        if not line: 
            continue 

        if line.startswith("#"):
            continue

        if line.startswith("1)reguladorId"): 
            continue

        fields = line.split("\t")
        
        if len(fields) <= 5: 
            continue

        TF= fields[1]
        gene= fields[4]
        effect= fields[5]

        if effect not in ["+", "-"]:
            continue

        interactions.append((TF, gene, effect))