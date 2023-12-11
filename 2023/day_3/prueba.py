def encontrar_conjuntos(matriz):
    conjuntos = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j].isdigit():
                conjunto = []
                dfs(i, j, matriz, conjunto)
                conjuntos.append(conjunto)

    return conjuntos

def dfs(i, j, matriz, conjunto):
    if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]) and matriz[i][j].isdigit():
        # Agregar el número al conjunto y marcar como visitado
        conjunto.append(matriz[i][j])
        matriz[i][j] = '.'

        # Explorar en las cuatro direcciones adyacentes
        dfs(i + 1, j, matriz, conjunto)
        dfs(i - 1, j, matriz, conjunto)
        dfs(i, j + 1, matriz, conjunto)
        dfs(i, j - 1, matriz, conjunto)

# Tu matriz original ajustada
matriz_original = [
    ['.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','8','*','5','.','.','.','4','1','.'],
    ['.','.','.','*','.','.','.','.','.','.','.','.'],
    ['.','.','.','2','7','.','.','.','.','.','.','.']
]

# Encontrar conjuntos
conjuntos = encontrar_conjuntos(matriz_original)

# Imprimir conjuntos
for conjunto in conjuntos:
    print(conjunto)
