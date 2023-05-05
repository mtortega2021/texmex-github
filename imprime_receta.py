# Abre el archivo en modo lectura
archivo = open("texmex-lsis/recetas.md", "r")

# Lee el contenido del archivo y lo guarda en una variable
contenido = archivo.read()

# Imprime el contenido del archivo por la terminal
print(contenido)

# Cierra el archivo
archivo.close()
