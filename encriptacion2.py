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
        else:
            n = ord(car)
        encriptada += str(n)
    return int(encriptada)


clave = input("Ingrese su clave: ")
encriptacion = encripta(clave)
print("encriptación:", encriptacion)


# Esta versión de la función itera sobre cada carácter en la cadena de entrada. Si el carácter es una letra, se obtiene su valor ASCII y se aplica la encriptación de forma diferente para mayúsculas y minúsculas. Si el carácter es un dígito, se aplica la misma encriptación que en la versión original. Si el carácter es otro tipo de símbolo, se utiliza su valor ASCII directamente.

# Es importante tener en cuenta que esta forma de encriptación no es muy segura y puede ser vulnerada fácilmente por alguien que tenga acceso a la función encripta. Si necesitas una encriptación más segura, es recomendable utilizar alguna biblioteca criptográfica estándar.
