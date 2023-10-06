def mediana_de_tres(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número: "))

        mediana = mediana_de_tres(num1, num2, num3)
        print(f"La mediana de los números {num1}, {num2} y {num3} es {mediana}")
    except ValueError:
        print("Por favor, ingrese números válidos.")
