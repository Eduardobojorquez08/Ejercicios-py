def es_palindromo(palabra):
    es_palindromo = palabra == palabra [::-1]
    return es_palindromo
print(es_palindromo("radar"))
print(es_palindromo("python"))