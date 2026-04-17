# Casos de prueba

## Caso 1

Entrada:

```

interacciones = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-"),
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"), 
]

```

Salida esperada:

```

Gen | No. de genes que regula | Genes regulados
AraC | 2 | araA, araB
CRP | 2 | lacY, lacZ
LexA | 1 | recA

```

**Extensión**

## Datos 1

Entrada:

```

interactions = [
    ("AraC", "araA", "+"),
    ("AraC", "araB", "-"),
    ("LexA", "recA", "-")
]

```

Salida esperada:

```

TF | No. de genes que regula | Genes regulados | + | -
AraC | 2 | araA, araB | 1 | 1
LexA | 1 | recA | 0 | 1

```
## Datos 2

Entrada:

```

interactions = [
    ("CRP", "lacZ", "+"),
    ("CRP", "lacY", "+"),
    ("CRP", "lacA", "+")
]

```

Salida esperada:

```

TF | No. de genes que regula | Genes regulados | + | -
CRP | 3 | lacZ, lacY, lacA | 3 | 0

```

## Datos 3

Entrada:

```

interactions = [
    ("LexA", "recA", "-"),
    ("LexA", "umuC", "-"),
    ("AraC", "araE", "+"),
    ("AraC", "araA", "-")
]

```

Salida esperada:

```()

TF | No. de genes que regula | Genes regulados | + | -
LexA | 2 | recA, umuC | 0 | 2
AraC | 2 | araE, araA | 1 | 1

```

## Command Line Interface (CLI)

Caso: Correr el programa con paso de argumentos: 

Entrada: 

```bash
uv run python regulon_summary.py input.txt output.txt 

uv run python regulon_sumary.py NetworkRegulatorGene.tsv tf_summary.txt 
```

Resultado: 
El programa lea el archivo de entrada y genere el resultado con el no,bre que se le paso como argumento. 