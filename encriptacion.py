# Literal a)
def encripta(entero):
    cadena = str(entero)  # "1254"
    n1 = str((int(cadena[0]) + 7) % 10)
    n2 = str((int(cadena[1]) + 7) % 10)
    n3 = str((int(cadena[2]) + 7) % 10)
    n4 = str((int(cadena[3]) + 7) % 10)
    respuesta = int(n3 + n4 + n1 + n2)
    return respuesta  # 2189


# literal b)
clave = int(input("Ingrese su clave: "))
encriptacion = encripta(clave)
print("encriptación:", encriptacion)

# El código consta de dos partes:

#     En la primera parte(literal a), se define una función llamada encripta que toma un argumento entero. La función convierte entero en una cadena de caracteres, luego aplica una operación de encriptación a cada dígito de la cadena y finalmente devuelve un número entero como resultado de concatenar los dígitos encriptados en un orden específico.

#     En la segunda parte(literal b), se solicita al usuario que ingrese una clave y se almacena en la variable clave. Luego se llama a la función encripta con clave como argumento y se almacena el resultado en la variable encriptacion. Finalmente, se imprime el mensaje "encriptación:" seguido del valor de encriptacion.

# En resumen, el código toma una clave numérica, la encripta usando la función encripta y muestra la encriptación resultante en la pantalla.
