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
    

    if not os.path.exists(filename):
        raise RuntimeError(f"Error: Archivo no existe --> {filename}")
    if os.path.getsize(filename) == 0:
        raise RuntimeError(f"Error: Archivo vacío --> {filename}")

    interacciones = []

    try:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("1)reguladorId"):
                    continue
                fields = line.split("\t")
                if len(fields) <= 5:
                    continue
                TF = fields[1].strip()
                gene = fields[4].strip()
                efecto = fields[5].strip()
                if efecto not in ["+", "-"]:
                    continue
                interacciones.append((TF, gene, efecto))
    except PermissionError:
        raise RuntimeError(f"Error: No hay permisos para leer {filename}")
    except UnicodeDecodeError:
        raise RuntimeError(f"Error: El archivo {filename} no es UTF-8 válido")
    except OSError as e:
        raise RuntimeError(f"Error I/O al leer {filename}: {e}")

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

    try:
        with open(output_file, "w") as out:
            # Cabecera exacta del original
            out.write("TF\tTotal genes\tActivados\tReprimidos\tTipo\tGenes\n")
            for tf in sorted(regulon):
                genes = regulon[tf]
                total = len(genes)
                mas = clasificacion.get(tf, {}).get("+", 0)
                menos = clasificacion.get(tf, {}).get("-", 0)
                # Determinar tipo
                if mas == 0:
                    tipo = "represor"
                elif menos == 0:
                    tipo = "activador"
                else:
                    tipo = "dual"
                lista_genes = ", ".join(sorted(genes))
                out.write(f"{tf}\t{total}\t{mas}\t{menos}\t{tipo}\t{lista_genes}\n")
    except PermissionError:
        raise RuntimeError(f"Error: No hay permisos para escribir {output_file}")
    except OSError as e:
        raise RuntimeError(f"Error I/O al escribir {output_file}: {e}")


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
    args = parse_arguments()

    # Crear directorio de salida si no existe
    output_dir = os.path.dirname(args.output_file)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except PermissionError:
            print(f"Error: No hay permisos para crear el directorio {output_dir}")
            exit(1)

    try:
        interacciones = load_interacciones(args.input_file)
        regulon, clasificacion = build_regulon_and_clasificacion(interacciones)

        # Filtrar por min_genes (como en el original)
        regulon_filtrado = {}
        clasificacion_filtrada = {}
        for tf, genes in regulon.items():
            if len(genes) >= args.min_genes:
                regulon_filtrado[tf] = genes
                clasificacion_filtrada[tf] = clasificacion[tf]

        generate_output(regulon_filtrado, clasificacion_filtrada, args.output_file)
        print(f"Resumen del regulón guardado en: {args.output_file}")

    except RuntimeError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()




