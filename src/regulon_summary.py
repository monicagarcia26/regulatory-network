import argparse
import os

def load_interacciones(filename):
    # ========================================
    # Lectura de datos desde un archivo TSV. 
    #=========================================

    #===========================================
    # Responsabilidad de este bloque de código: Leer el archivo "NetworkRegulatorGene.tsv".
    # Entrada: Archivo de texto con información sobre reguladores, genes y efectos.
    # Salida: Lista de tuplas con (TF, gene, efecto) para cada interacción  
    #============================================

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

    return interacciones

def build_regulon_and_clasificacion(interacciones):


    # ===========================================
    # Construir diccionario de TF y lista de genes
    # ===========================================

    # ==========================================
    # Responsabilidad de este bloque de código: Construir un diccionario que mapea cada TF a una lista de genes que regula, y otro diccionario para contar los efectos positivos y negativos.
    # Entrada: Lista de tuplas con (TF, gene, efecto) para cada interacción.
    # Salida: Dos diccionarios: uno que mapea cada TF a una lista de genes regulados, y otro que mapea cada TF a un conteo de efectos positivos y negativos.
    # ==========================================

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
    
    return regulon, clasificacion


def generate_output(regulon, clasificacion, output_file):

    # ===========================================
    # Generación de un archivo de salida.
    # ===========================================

    # ==========================================
    # Responsabilidad de este bloque de código: Generar un archivo de texto con un resumen de los reguladores, incluyendo el número de genes que regulan, los genes regulados y la clasificación de efectos.
    # Entrada: Dos diccionarios: uno que mapea cada TF a una lista de genes regulados, y otro que mapea cada TF a un conteo de efectos positivos y negativos.
    # Salida: Archivo de texto con un resumen de los reguladores.   
    # ==========================================

    with open(output_file, "w") as out:
        out.write("TF | No. de genes que regula | Genes regulados | + | -\n")
        for tf in regulon:
            numero = len(regulon[tf])
            genes = ", ".join(regulon[tf]) # convierte la lista de genes en texto separado por comas.  
            mas = clasificacion.get(tf, {}).get("+", 0)
            menos = clasificacion.get(tf, {}).get("-", 0)
            out.write(f"{tf} | {numero} | {genes} | {mas} | {menos}\n")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Lee un archivo TSV con interacciones reguladoras y muestra un resumen de los reguladores y sus efectos."
    )

    parser.add_argument(
        "input_file", help="Archivo de entrada en formato TSV con las interacciones reguladoras."
    )
    parser.add_argument(
        "output_file", help="Archivo de salida donde se guardará el resumen de los reguladores."
    )
    parser.add_argument(
        "--min_genes", type=int, default=1, help="Número mínimo de genes regulados para incluir un regulador en el resumen."
    )

    args = parser.parse_args()  # leer los argumentos desde la línea de comandos

    if not os.path.isfile(args.input_file):
        parser.error(f"El archivo de entrada '{args.input_file}' no existe o no es un archivo válido.")

    return args


def main():

    #Función principal que orquesta la ejecución del programa. Lee los argumentos, carga las interacciones, construye el regulón y la clasificación, y genera el archivo de salida.

    args = parse_arguments()

    print(args)
    print(f"Archivo de entrada: {args.input_file}")
    print(f"Archivo de salida: {args.output_file}")
    print(f"Número mínimo de genes regulados: {args.min_genes}")

    interacciones = load_interacciones(args.input_file)
    regulon, clasificacion = build_regulon_and_clasificacion(interacciones)
    generate_output(regulon, clasificacion, args.output_file)


if __name__ == "__main__":
    main()




