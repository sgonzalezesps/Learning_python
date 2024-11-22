# funcion startswith y endswith

frase = ("El lobo aulla a la luna")

comienzo = bool( frase.startswith("El",0,10))
print(comienzo)

fin = frase.endswith("luna",5, 23)
print(fin)
