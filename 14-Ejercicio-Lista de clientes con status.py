clientes = ["Eduardo" , "Alexandra" , "Emiliano"]
servicios = ["Plomeria", "Carpintero", "Chef"]
pagado = [True, False , True]

for i in range(len(clientes)):
    if pagado[i] == True:
        status = "Pagado"
    else:
        status = "No pagado"
    print(f"{i+1}: {clientes[i]} - {servicios[i]} - {status}")