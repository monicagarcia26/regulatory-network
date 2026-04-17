import argparse

parser = argparse.ArgumentParser(
    description="Lee un archivo TSV con interacciones reguladoras y muestra un resumen de los reguladores y sus efectos."
    )  

# definir argumentos 

parser.add_argument(
    "input_file", help="Archivo de entrada en formato TSV con las interacciones reguladoras."
    )
parser.add_argument(
    "output_file", help="Archivo de salida donde se guardará el resumen de los reguladores."
    )
parser.add_argument(
    "--min_genes", type=int, default=1, help="Número mínimo de genes regulados para incluir un regulador en el resumen."
    )

args = parser.parse_args() # leer los argumentos desde la línea de comandos

print(args) 

print(f"Archivo de entrada: {args.input_file}")
print(f"Archivo de salida: {args.output_file}")
print(f"Número mínimo de genes regulados: {args.min_genes}")
