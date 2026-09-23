lista = []

# Pedir 5 cadenas
for i in range(5):
    texto = input("Ingresa una cadena de texto: ")
    lista.append(texto)

# Pedir los 3 índices
indice1 = int(input("Ingresa el primer número (0-4): "))
indice2 = int(input("Ingresa el segundo número (0-4): "))
indice3 = int(input("Ingresa el tercer número (0-4): "))

# Obtener las cadenas usando los índices
cadena1 = lista[indice1]
cadena2 = lista[indice2]
cadena3 = lista[indice3]

# Concatenar y mostrar
resultado = cadena1 + cadena2 + cadena3

print("Cadena resultante:", resultado)