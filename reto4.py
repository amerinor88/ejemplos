# Preguntamos al usuario por una frase
frase = input("Ingresa una frase: ")

# Invertimos la frase
frase_invertida = ""

# Recorremos la frase de atrás hacia adelante
for i in range(len(frase)-1, -1, -1):
    # Añadimos cada letra a la frase invertida
    frase_invertida += frase[i]

# Imprimimos la frase invertida
print(frase_invertida)
