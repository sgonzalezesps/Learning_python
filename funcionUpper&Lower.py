#metodos upper y lower

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nombre_completo = f"{nombre} {apellido}"

if nombre_completo.isupper() == False:
    print("Convirtiendo cadena a mayusculas...")
    nombre_completo = nombre_completo.upper()
    print(nombre_completo)
else:
    print("La cadena ya tiene formato de mayusculas")
    print(nombre_completo)

if nombre_completo.islower() == False:
    print("Convirtiendo cadena a minusculas...")
    nombre_completo = nombre_completo.lower()
    print(nombre_completo)
else:
    print("La cadena ya tiene formato de mayusculas")
    print(nombre_completo)
