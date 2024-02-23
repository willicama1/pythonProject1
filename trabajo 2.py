def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenar_fila(uea, fila):
    uea[fila] = bubble_sort(uea[fila])
    return uea

# Matriz original
uea = [[5, 2, 9], [8, 1, 4], [7, 6, 3]]
print("Matriz original:")
for fila in uea:
    print(fila)

# Ordenar la segunda fila (índice 1)
matriz_ordenada = ordenar_fila(uea, 1)
print("\nMatriz con la segunda fila ordenada:")
for fila in matriz_ordenada:
    print(fila)