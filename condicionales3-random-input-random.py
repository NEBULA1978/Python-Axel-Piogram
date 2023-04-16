import random

resultados = []

# Genera un número aleatorio entre 1 y 20 (puedes ajustar el rango)
cantidad_numeros = random.randint(1, 20)

print(f"Se generarán {cantidad_numeros} números aleatorios.")

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
# En este código, la variable cantidad_numeros se asigna a un número aleatorio entre 1 y 20 (puedes ajustar este rango según tus necesidades). Luego, el programa generará e imprimirá esa cantidad de números aleatorios junto con sus respectivos resultados, sin requerir la interacción del usuario.
