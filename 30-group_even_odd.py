numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def agrupar_pares_impares(numeros):
    resultado = {"pares": [], "impares": []}
    for numero in numeros:
        if numero % 2 == 0:
            resultado["pares"].append(numero)
        else:
            resultado["impares"].append(numero)
    return resultado
print(agrupar_pares_impares(numeros))