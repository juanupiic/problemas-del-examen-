def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def nextPrime(n):
    if n <= 1:
        n = 2  # El primer número primo es 2
    else:
        n += 1  # Comenzamos la búsqueda desde el siguiente número
    while True:
        if es_primo(n):  # Cambio de is_prime a es_primo
            return n
        n += 1

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número entero: "))
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero válido.")

    try:
        num = int(input("Ingrese un número entero: "))
        if num < 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            primer_primo_mayor = nextPrime(num)
            print(f"El primer número primo mayor que {num} es {primer_primo_mayor}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

