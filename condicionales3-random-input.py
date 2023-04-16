import random

resultados = []

cantidad_numeros = int(
    input("Ingrese la cantidad de números aleatorios a generar: "))

for _ in range(cantidad_numeros):
    # Puedes ajustar el rango de números aleatorios aquí
    numero = random.randint(-1000, 1000)
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

    print(f"Número: {numero}, Resultado: {resultado}")
    resultados.append(resultado)

print("Resultados:")
for i, res in enumerate(resultados):
    print(f"{i + 1}. {res}")
# Este código solicita al usuario la cantidad de números aleatorios a generar y luego crea un bucle for para generar esa cantidad de números. Los números aleatorios se generan utilizando la función randint del módulo random. Puedes ajustar el rango de números aleatorios modificando los argumentos de la función randint.
