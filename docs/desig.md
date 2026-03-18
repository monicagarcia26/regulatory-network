# Diseño de la solución

## Algoritmo 
- Lista/ estructura de reguladores (sin repeticiones). 
- Lista de genes del regulador (sin repeticiones)*
- Recorrer todas las interacciones (línea). 
- Para cada interacción
  - Obtener el TF 
  - Obtener el gene
  - Si el TF no está en la lista de reguladores:
    - Guardar el TF en una estructura/lista
  - Si el gene no está en la lista de genes regulados por regulador
    - Guarda el gene asociado 

- Recorrer toda la lista de los reguladores 
 - Contar los genes de la lista de genes regulados por el TF 
 - Imprime regulador, conteo, lista de genes 

