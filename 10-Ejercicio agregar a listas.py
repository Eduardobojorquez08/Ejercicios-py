servicios = []

for i in range(3):
    servicio = input("¿Qué servicios quieres agendar? ")
    servicios.append(servicio)
    
print("Servicios agendados:")
for i in range(1, 4):
    print(f"{i}: {servicios[i-1]}")
  