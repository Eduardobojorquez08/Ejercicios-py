servicios = ["Fumigacion", "Plomeria" , "Carpintero"]
precios = [600, 400 , 350]
print(f"Tienes {len(servicios)} Servicios disponibles:")

for i in range(len(servicios)):
    print(f"{i+1}: {servicios[i]}  ${precios[i]}")