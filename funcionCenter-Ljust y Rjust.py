#metodos center, ljust y rjust

palabra = input("Ingresa una palabra para centrar: ")
palabra2 = input("Ingresa una palabra para alinear a la izquierda: ")
palabra3 = input("Ingresa una palabra para alinear a la derecha: ")

palabra = palabra.center(10,"=")
print(f"La palabra centrada es\n {palabra}")

palabra2 = palabra2.ljust(10,"-")
print(f"La palabra alineada a la izquierda es\n {palabra2}")

palabra3 = palabra3.rjust(10,"_")
print(f"La palabra alineada a la derecha es\n {palabra3}")
