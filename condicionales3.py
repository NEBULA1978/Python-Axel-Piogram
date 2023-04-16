resultados = []

while True:
    numero = input("Ingrese un número o 'salir' para terminar: ")
    if numero.lower() == 'salir':
        break

    numero = int(numero)
    resultado = ""

    # Opcion 2
    if numero == 0:
        resultado = "Neutro"
    else:
        esPar = numero % 2 == 0
        if esPar:
            if numero > 0:
                resultado = "Positivo par"
            else:
                resultado = "Negativo par"
        else:
            if numero > 0:
                resultado = "Positivo impar"
            else:
                resultado = "Negativo impar"

    print(resultado)
    resultados.append(resultado)

print("Resultados:")
for i, res in enumerate(resultados):
    print(f"{i + 1}. {res}")
# Este código también permite al usuario ingresar números múltiples veces y almacena los resultados en la lista resultados utilizando la Opción 2. Cuando el usuario ingresa 'salir', el programa termina y muestra todos los resultados almacenados.
