#funcion len

palabra = input("Ingresa una palabra: ")

longitud = len(palabra)

if longitud >= 8:
    print("Se ingreso una palabra larga, con un total de",longitud,"caracteres")
else:
    print("Se ingreso una palabra corta, con un total de",longitud,"caracteres")

