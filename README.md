# Regulatory Network Analysis

En biología molecular, un regulón es el conjunto de genes que están bajo el control de un mismo factor de transcripción (TF). Es decir, todos los genes que un TF regula (ya sea activándolos o reprimiéndolos) forman parte de su regulón.

Este proyecto analiza datos de una red regulatoria para generar un resumen de regulones a partir de un archivo TSV de interacciones TF-gen.


## Ejecución

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

## Estructura del proyecto

```
regulatory-network/
├── data/
│   └── raw/
│       ├── NetworkRegulatorGene.tsv
│       └── README.md
├── docs/
├── results/  # Se crea automáticamente
├── src/
│   └── regulon_summary.py
├── pyproject.toml
└── README.md

```
