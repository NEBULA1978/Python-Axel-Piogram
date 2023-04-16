resultados = []

while True:
    numero = input("Ingrese un número o 'salir' para terminar: ")
    if numero.lower() == 'salir':
        break

    numero = int(numero)
    resultado = ""

    # Opcion 1
    esPar = numero % 2 == 0
    if numero == 0:
        resultado = "Neutro"
    elif esPar and numero > 0:
        resultado = "Positivo Par"
    elif not esPar and numero > 0:
        resultado = "Positivo Impar"
    elif esPar and numero < 0:
        resultado = "Negativo Par"
    elif not esPar and numero < 0:
        resultado = "Negativo Impar"

    print(resultado)
    resultados.append(resultado)

print("Resultados:")
for i, res in enumerate(resultados):
    print(f"{i + 1}. {res}")
# Este código permite al usuario ingresar números múltiples veces y almacena los resultados en la lista resultados. Cuando el usuario ingresa 'salir', el programa termina y muestra todos los resultados almacenados.
