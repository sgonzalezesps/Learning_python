#convsersor (if anidados)

nombre = input("Ingresa tu nombre: ")

print("Bienvenido",nombre)

print("----- Menú de opciones -----")
print("1.- Convertir números a letras\n2.- Convertir palabras a números\n")
numero_opcion = float(input("Ingresa el número de opción que deseas: "))

if numero_opcion == 1:
    numero = int(input("Ingresa el número a convertir del 1 al 3: "))
    if numero == 1:
        print("El numero ingresado es el uno")
    elif numero == 2:
        print("El numero ingresado es el dos")
    elif numero == 3:
        print("El numero ingresado es el tres")
    else:
        print("Número fuera de rango")

else:
    palabra = input("Ingresa la palabra a convertir [uno, dos o tres]: ")
    palabra = palabra.lower()
    if palabra == "uno":
        print("El numero ingresado es el 1")
    elif palabra == "dos":
        print("El numero ingresado es el 2")
    elif palabra == "tres":
        print("El numero ingresado es el tres")
    else:
        print("Número no reconocido")
    
print("FIN.")
