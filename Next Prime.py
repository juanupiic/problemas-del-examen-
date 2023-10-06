import random

def generar_contrasena_aleatoria():
    longitud = random.randint(7, 10)  # Generar una longitud aleatoria entre 7 y 10 caracteres
    contrasena = ""
    
    for _ in range(longitud):
        caracter_aleatorio = chr(random.randint(33, 126))  # Generar un carácter aleatorio en el rango ASCII
        contrasena += caracter_aleatorio
    
    return contrasena

if __name__ == "__main__":
    contrasena_generada = generar_contrasena_aleatoria()
    print(f"Contraseña generada aleatoriamente: {contrasena_generada}")
