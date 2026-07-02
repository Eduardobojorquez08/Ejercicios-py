estudiantes = [
    ["Ana", 95],
    ["Luis", 72],
    ["Marta", 88],
    ["Carlos", 60],
    ["Sofía", 91],
    ["Pedro", 78]
]

def agrupar_por_rango(estudiante):
    resultado = {}

    for nombre, calificacion in estudiantes:
        if calificacion >= 90:
          letra = "A"
        elif calificacion >= 80:
           letra = "B"
        elif calificacion >= 70:
           letra = "C"
        elif calificacion >= 60:
           letra = "D"
        else:
           letra = "F"
        
        if letra in resultado:
           resultado[letra].append(nombre)
        else:
           resultado[letra] = [nombre]

    return resultado
print(agrupar_por_rango(estudiantes))


        
            



