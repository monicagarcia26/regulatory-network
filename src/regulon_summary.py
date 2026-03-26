# Lectura de datos desde un archivo TSV. 

filename = "../data/raw/NetworkRegulatorGene.tsv"
interacciones = []  # Inicializar lista para almacenar interacciones

with open(filename) as f:
    
    for line in f:
        line = line.strip() # quita los saltos de línea.

        # Ignorar líneas vacías, comentarios y encabezados.

        if not line: 
            continue 

        if line.startswith("#"): # líneas que empiecen con #. 
            continue

        if line.startswith("1)reguladorId"): # si empieza así ignórala. 
            continue

        fields = line.split("\t") # separar por tabulaciones.

        # Validar que haya suficientes campos y que el efecto sea válido.
        
        if len(fields) <= 5: 
            continue

        TF= fields[1]
        gene= fields[4]
        efecto= fields[5]

        if efecto not in ["+", "-"]:
            continue

        interacciones.append((TF, gene, efecto))


# Construir diccionario de TF y lista de genes

regulon = {}

clasificacion = {}

for tf, gen, efecto in interacciones:
        if tf not in regulon:
            regulon[tf] = []
        
        if gen not in regulon[tf]:
            regulon[tf].append(gen)
        
        if tf not in clasificacion:
             clasificacion[tf]= { '+' : 0 , '-' : 0 }  #  cada tf apunta a un diccionario con conteo de efectos positivos y negativos. 
        if efecto == "+" or efecto == "-": 
            clasificacion[tf][efecto] += 1


# Generación de un archivo de salida.

with open("../results/regulon_summary_output.txt", "w") as out:
    out.write("TF | No. de genes que regula | Genes regulados | + | -\n")

    print("TF | No. de genes que regula | Genes regulados | + | -")
    for tf in regulon:
        numero = len(regulon[tf])
        genes = ", ".join(regulon[tf])
        mas = clasificacion.get(tf, {}).get("+", 0)
        menos = clasificacion.get(tf, {}).get("-", 0)
        linea = f"{tf} | {numero} | {genes} | {mas} | {menos}\n"
        out.write(linea)
        print(tf, "|", numero, "|", genes, "|", mas, "|", menos)
  