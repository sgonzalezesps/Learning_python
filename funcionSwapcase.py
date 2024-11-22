#metodo swapcase

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nombre_completo = f"{nombre} {apellido}"

print("Invirtiendo caracteres de la cadena...")
nombre_completo = nombre_completo.swapcase()
print(nombre_completo)
