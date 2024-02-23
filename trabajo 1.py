uea = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
buscar = 2

def universidad_uea(uea, valor):
    for u in range(len(uea)):
        for e in range(len(uea[u])):
            if uea[u][e] == valor:
                return True, (u, e)
    return False, None
encontrado, posicion = universidad_uea (uea, buscar)

if encontrado:
    print(f"El valor {buscar} se encontró en la posición {posicion} de la matriz.")
else:
    print(f"El valor {buscar} no se encontró en la matriz.")