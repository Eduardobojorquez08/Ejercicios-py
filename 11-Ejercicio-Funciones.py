def saludar_cliente(nombre):
    print(f"Hola {nombre}, Bienvenido a walletcontrol") #aca agregas el saludo 

clientes = ["Eduardo" , "Nicolas" , "Andres"]

for i in range(3):
    saludar_cliente(clientes[i])