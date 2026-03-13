# Diseño de la solución

## Algoritmo versión 1

1. Crear una lista de TFs encontrados.

2. Recorrer todas las interacciones.

3. Para cada interacción:
   - obtener el TF
   - si el TF no está en la lista, agregarlo.

4. Para cada TF encontrado:
   - crear una lista de genes
   - recorrer las interacciones
   - agregar genes asociados

5. Contar genes por TF.

6. Imprimir la tabla resumen.