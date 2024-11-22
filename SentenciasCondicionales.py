#Sentencias condicionales (promedio alumno)

nombre_alumno = input("Alumno, Ingresa tu nombre: ")

print("Bienvenido ",nombre_alumno)

calificacion_matematicas = float(input("Ingresa tu calificación de mátematicas: "))
calificacion_quimica = float(input("Ingresa tu calificación de química: "))
calificacion_biologia = float(input("Ingresa tu calificación de biología: "))

promedio = (calificacion_matematicas + calificacion_quimica + calificacion_biologia) / 3

if promedio >= 7:
    print("Felicidades ",nombre_alumno,", estás aprobado! :), con un promedio de: ",promedio)

print("FIN.")

