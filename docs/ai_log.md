# Interacción 1 

**Pregunta:**

si ya tengo este código cómo puedo imprimir mis resultados de la clasificación de cada TF?

**Respuesta**

```

# Imprimir la tabla final
print("TF | No. de genes que regula | Genes regulados | + | -")
for tf in regulon:
    numero = len(regulon[tf])
    genes = ", ".join(regulon[tf])
    mas = clasificacion.get(tf, {}).get("+", 0)
    menos = clasificacion.get(tf, {}).get("-", 0)
    print(tf, "|", numero, "|", genes, "|", mas, "|", menos)

```
# Interacción 2 

**Pregunta:** 

me ayudas a redactar el archivo README de regulo_summary.py para su ejecucuón, usando uv

**Respuesta** 

Para ejecutar el script de análisis de regulones:

```bash
uv run python src/regulon_summary.py
```

O si prefieres ejecutar directamente con uv:

```bash
uv run src/regulon_summary.py
```

## Datos de entrada

El script lee el archivo `data/raw/NetworkRegulatorGene.tsv` que debe contener:
- Columnas separadas por tabulaciones
- Campos: reguladorId, TF, gene, efecto (+ o -), etc.

## Salida

El script genera:
- Un archivo de salida: `results/regulon_summary_output.txt`
- Una tabla impresa en la terminal con:
  - TF: Factor de transcripción
  - No. de genes que regula: Cantidad de genes regulados
  - Genes regulados: Lista de genes
  - +: Conteo de efectos positivos
  - -: Conteo de efectos negativos

