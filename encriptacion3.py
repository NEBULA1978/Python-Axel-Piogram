def encripta(cadena):
    encriptada = ''
    for car in cadena:
        if car.isalpha():
            codigo = ord(car)
            if car.isupper():
                n = (codigo - 65 + 7) % 26 + 65
            else:
                n = (codigo - 97 + 7) % 26 + 97
        elif car.isdigit():
            n = (int(car) + 7) % 10
            if n < 10:
                n = f"0{n}"
        else:
            n = ord(car)
        encriptada += str(n)
    return encriptada


clave = input("Ingrese su clave: ")
encriptacion = encripta(clave)

with open("encript.txt", "a", encoding="utf-8") as archivo:
    archivo.write(encriptacion + "\n")

print("La clave se ha encriptado y guardado en el archivo 'encript.txt'")
password = input("Ingrese la contraseña para leer el archivo: ")

with open("encript.txt", "r", encoding="utf-8") as archivo:
    encriptacion_guardada = archivo.read().strip()

if password == clave:
    print("La contraseña es correcta. La encriptación es:", encriptacion_guardada)
else:
    print("La contraseña es incorrecta. No se puede leer la encriptación.")
# En este código, primero se define la función encripta() que toma una cadena y la encripta utilizando la misma técnica de la pregunta anterior. Luego, se solicita una clave al usuario y se encripta utilizando la función encripta(). La encriptación se guarda en un archivo llamado encript.txt.

# Después, se solicita una contraseña para leer la encriptación desde el archivo. Se lee la encriptación del archivo, se elimina cualquier caracter de salto de línea adicional utilizando el método strip() y se compara con la contraseña ingresada. Si la contraseña coincide con la clave original, se muestra la encriptación en la pantalla. Si la contraseña no coincide, se muestra un mensaje de error.
