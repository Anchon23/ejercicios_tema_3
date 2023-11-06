def determinante_matriz_recursivo(matriz):
    if len(matriz) != 3 or len(matriz[0]) != 3:
        return "La matriz debe ser de 3x3"
    
    if len(matriz) == 1:
        return matriz[0][0]
    
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante = 0
    for i in range(len(matriz)):
        cofactor = matriz[0][i] * determinante_matriz_recursivo(submatriz(matriz, 0, i))
        if i % 2 == 1:
            cofactor *= -1
        determinante += cofactor
    
    return determinante

def submatriz(matriz, fila, columna):
    return [row[:columna] + row[columna+1:] for row in (matriz[:fila] + matriz[fila+1:])]

matriz = [
    [4, 2, 1],
    [0, 6, 3],
    [1, 0, 2]
]

resultado = determinante_matriz_recursivo(matriz)
print("Determinante (Recursivo):", resultado)
