clientes = ["Eduardo", "María", "Alan", "Sofía", "Carlos"]  
servicios = ["plomeria", "limpieza", "electricidad", "plomeria", "limpieza"]   

busqueda = input("¿Qué servicio esta buscando?").lower()  

print(f"\nClientes con {busqueda}:")  

for i in range(len(servicios)):    
    if servicios[i] == busqueda:   
        print(f"- {clientes[i]}")    
        

