import random

horas = random.randint(30, 50)
valorHora = round(random.uniform(10, 20), 2)

print("Horas trabajadas:", horas)
print("Valor hora:", valorHora)

salarioBruto = 0
valorExtra = 0

if horas < 38:
    salarioBruto = horas * valorHora
else:
    salarioBruto = 37 * valorHora  # Salario horas normales # 370
    horasExtra = horas - 37  # 3
    valorExtra = (valorHora*1.50) * horasExtra  # 45

if salarioBruto > 1600:
    salarioBruto -= salarioBruto * 0.10

print('Salario Neto:', round(salarioBruto + valorExtra, 2))


a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

if a == b == c:
    print("Los números son iguales")
else:
    print("Los números no son iguales")

print("a =", a)
print("b =", b)
print("c =", c)
# Este código genera valores aleatorios para las horas trabajadas y el valor hora, y luego calcula el salario neto utilizando la misma lógica que el código original.

# También genera valores aleatorios para a, b y c, y luego verifica si son iguales o no. Al final, se imprimen todos los valores generados y los resultados de los cálculos.

# Resultado por consola:
# <◂> python3 Ejercicio3-random.py
# Horas trabajadas: 37
# Valor hora: 19.62
# Salario Neto: 725.94
# Los números no son iguales
# a = 5
# b = 9
# c = 8
# <◂>
