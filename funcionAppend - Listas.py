# funcion Append - listas

print("Añadiendo un elemento a una lista")
letras = ["a","b","c","d"]
print(f"Lista: {letras}")
letras.append("e")
print(f"Lista: {letras}")


print("\nAñadiendo elementos a una lista")
letras = ["a","b","c","d"]
print(f"Lista: {letras}")
letras.append("e")
letras.append("f")
letras.append("g")
print(f"Lista: {letras}")


print("\nAñadiendo elementos a una lista de distinto tipo de dato")
lista_letras = ["a","b","c","d"]
print(f"Lista: {letras}")
letras.append(5)
letras.append(2.3)
letras.append(True)
print(f"Lista: {letras}")
