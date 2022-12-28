# Preguntamos al usuario por una frase y una vocal
frase = input("Ingresa una frase: ")
vocal = input("Ingresa una vocal: ")

# Verificamos que la vocal sea una de las cinco vocales
if vocal.lower() in ['a', 'e', 'i', 'o', 'u']:
    # Reemplazamos la vocal por su versión en mayúsculas en la frase
    frase_modificada = frase.replace(vocal, vocal.upper())
    print(frase_modificada)
else:
    # Si la vocal no es una de las cinco vocales, mostramos un mensaje de error
    print("La vocal introducida no es válida")
