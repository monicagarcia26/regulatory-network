# ========================================
# Lectura de datos desde un archivo TSV. 
#=========================================

#===========================================
# Responsabilidad de este bloque de código: Leer el archivo "NetworkRegulatorGene.tsv".
# Entrada: Archivo de texto con información sobre reguladores, genes y efectos.
# Salida: Lista de tuplas con (TF, gene, efecto) para cada interacción  
#============================================

def load_interacciones(filename):
    """Carga las interacciones desde un archivo TSV y devuelve una lista de tuplas (TF, gene, efecto) para cada interacción válida."""
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


def main():
    """Función principal que orquesta el flujo del programa."""
    try:
        print("Iniciando análisis de regulon...")
        
        # Configurar rutas de entrada y salida
        filename = "../data/raw/NetworkRegulatorGene.tsv"
        output_file = "../results/regulon_summary_output.txt"
        
        # Cargar interacciones desde el archivo
        print(f"Cargando interacciones desde {filename}...")
        interacciones = load_interacciones(filename)
        print(f"✓ Se cargaron {len(interacciones)} interacciones.")
        
        # Construir diccionarios de regulon y clasificación
        print("Construyendo diccionarios de TF y clasificación...")
        regulon, clasificacion = build_regulon_and_clasificacion(interacciones)
        print(f"✓ Se identificaron {len(regulon)} factores de transcripción (TF).")
        
        # Generar archivo de salida
        print(f"Generando salida en {output_file}...")
        generate_output(regulon, clasificacion, output_file)
        print(f"✓ Análisis completado exitosamente.")
        print(f"✓ Archivo de salida: {output_file}")
        
    except FileNotFoundError as e:
        print(f"✗ Error: No se encontró el archivo - {e}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")


if __name__ == "__main__":
    main()


