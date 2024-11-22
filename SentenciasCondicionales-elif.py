#Sentencias condicionales (promedio alumno con elif)

nombre_alumno = input("Alumno, Ingresa tu nombre: ")

print("Bienvenido ",nombre_alumno)

calificacion_matematicas = float(input("Ingresa tu calificación de mátematicas: "))
calificacion_quimica = float(input("Ingresa tu calificación de química: "))
calificacion_biologia = float(input("Ingresa tu calificación de biología: "))

promedio = (calificacion_matematicas + calificacion_quimica + calificacion_biologia) / 3

if promedio >= 9:
    print("Felicidades",nombre_alumno,",estás aprobado con excelencia! :D, con un promedio de: ",round(promedio,2))
elif promedio >=7:
    print("Felicidades",nombre_alumno,",estás aprobado! :), con un promedio de: ",round(promedio,2))
else:
    print("Lo siento",nombre_alumno,",estás reprobado! :(, con un promedio de: ",round(promedio,2))

print("FIN.")
