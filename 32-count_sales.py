ventas = ["manzana", "pan", "leche", "manzana", "pan", "manzana", "manzana", "pan", "leche", "queso",]

def contar_ventas(ventas):
    ventas_totales = {}
    for vendido in ventas:
        if vendido in ventas_totales:
            ventas_totales[vendido] += 1
        else:
            ventas_totales[vendido] = 1
    return ventas_totales
print(contar_ventas(ventas))