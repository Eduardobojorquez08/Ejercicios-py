import random 

numero_secreto = random.randint(1, 100)
intentos = 0

print(" Intenta adivinar el número en el que estoy pensando del 1 al 100: ")

while True:
    try:
        intento = int(input("¿Cual crees que es?"))
        intentos += 1
    except ValueError:
        print("Ingresa solo números")
        continue

    if intento == numero_secreto:
        print(" Has encontrado el Número secreto!")
        print(f"Lo lograste en {intentos} intentos!")
        break
    elif intento > numero_secreto:
        print("El número es demasiado alto, intenta con un número más bajo")
    elif intento < numero_secreto:
        print("El número es demasiado bajo, intenta con un número más alto")