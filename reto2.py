# Preguntamos al usuario por su nombre completo
nombre_completo = input("Ingresa tu nombre completo: ")

# Dividimos el nombre completo en nombre y apellido
nombre, apellido_paterno, apellido_materno = nombre_completo.split()

# Imprimimos el nombre completo tres veces
# Primera vez: con el apellido paterno en minúsculas y el resto en mayúsculas
print(nombre.upper() + " " + apellido_paterno.lower() +
      " " + apellido_materno.upper())

# Segunda vez: con apellidos en mayúsculas y nombre en minúsculas
print(nombre.lower() + " " + apellido_paterno.upper() +
      " " + apellido_materno.upper())

# Tercera vez: con mayúsculas en cada letra inicial del apellido y nombre en minúsculas
print(apellido_paterno.title() + " " +
      apellido_materno.title() + " " + nombre.lower())
