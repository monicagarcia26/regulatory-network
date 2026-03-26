# Lectura de datos desde un archivo TSV. 

filename = "data/raw/Network_RegulatorGene.tsv"

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
        effect= fields[5]

        if effect not in ["+", "-"]:
            continue

        interactions.append((TF, gene, effect))


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


# Imprimir la tabla final

print("TF | No. de genes que regula | Genes regulados | + | -")
for tf in regulon:
    numero = len(regulon[tf])
    genes = ", ".join(regulon[tf])
    mas = clasificacion.get(tf, {}).get("+", 0)
    menos = clasificacion.get(tf, {}).get("-", 0)
    print(tf, "|", numero, "|", genes, "|", mas, "|", menos)

