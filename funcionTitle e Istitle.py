#metodos title e istitle

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nombre_completo = f"{nombre} {apellido}"

if nombre_completo.istitle() == False:
    print("Convirtiendo cadena a titulo...")
    nombre_completo = nombre_completo.title()
    print(nombre_completo)
else:
    print("La cadena ya tiene formato de titulo")
    print(nombre_completo)
