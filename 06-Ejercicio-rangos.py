calificacion = int(input("Escribe una calificacion del 0 al 100: "))

if 90 <= calificacion <= 100:
  print("Excelente")

elif 70 <= calificacion <= 89:
  print("Aprobado")

elif 60 <= calificacion <= 69:
  print("Suficiente")

else:
  print("Reprobado")