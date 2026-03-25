
# Datos de ejemplo:

interacciones = [
    ("TF1", "GeneA", "+"),
    ("TF1", "GeneB", "-"),
    ("TF2", "GeneC", "+"),
    ("TF2", "GeneD", "+"),
    ("TF3", "GeneE", "-"),
    ("TF3", "GeneF", "-"),
    ("TF3", "GeneG", "+")
]

# Construir diccionario de TF y lista de genes

regulon = {}

clasificacion = {}

for tf, gen, efecto in interacciones:
        if tf not in regulon:
            regulon[tf] = []
        
        if gen not in regulon[tf]:
            regulon[tf].append(gen)
        
        if tf not in clasificacion:
             clasificacion[tf]= { '+' : 0 , '-' : 0 }
        if efecto in { '+', '-' }: 
            clasificacion[tf][efecto] += 1


# Imprimir la tabla final

print("TF | No. de genes que regula | Genes regulados | + | -")
for tf in regulon:
    numero = len(regulon[tf])
    genes = ", ".join(regulon[tf])
    mas = clasificacion.get(tf, {}).get("+", 0)
    menos = clasificacion.get(tf, {}).get("-", 0)
    print(tf, "|", numero, "|", genes, "|", mas, "|", menos)

