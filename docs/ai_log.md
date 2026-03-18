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