print("---Adicion:")

mensaje = "Hola"
mensaje += " "
mensaje += "Sebastian"
print(mensaje)

print("---Concatenacion:")

mensajeDos = "Hola"
espacio = " "
nombre = "Sebastian"
print(mensajeDos + espacio + nombre)

print("---Concatenacion con numeros y texto:")
numeroUno = 5
numeroDos = 10
resultado = numeroUno + numeroDos
print("El resultado es: " + str(resultado))


print("---Buscando posicion de subcadena")
mensajeTres = "Hola Sebastian"
busquedaSubcadena = mensajeTres.find("Sebastian")
print(busquedaSubcadena)

print("---Extrayendo subcadena")
mensajeCuatro = "Hola Sebastian"
extraerSubcadena = mensajeCuatro[5:14]
print(extraerSubcadena)

print("---Comparacion")
mensajeCinco = "Hola"
mensajeSeis = "Hola"

print(mensajeCinco == mensajeSeis)



