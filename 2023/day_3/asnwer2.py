from config import configs_2 as configs

def itsNumber(data):
    try:
        int(data)
        return True
    except:
        return False

def itsSymbol(data,symbol):
    if(not(itsNumber(data)) and data == symbol):
        return True
    return False

def extractNumber(matrix, matrixRef, positionA, positionB):
    if matrixRef[positionA][positionB]:
        return -1, matrixRef

    number = ""
    wleft = positionB

    try:
        while itsNumber(matrix[positionA][wleft]) and wleft != -1:
            number = matrix[positionA][wleft] + number
            matrixRef[positionA][wleft] = True
            wleft -= 1
    except IndexError:
        pass

    try:
        wright = positionB + 1
        while itsNumber(matrix[positionA][wright]) and wright != -1:
            number += matrix[positionA][wright]
            matrixRef[positionA][wright] = True
            wright += 1
    except IndexError:
        pass

    # Verificar si la cadena no está vacía antes de convertirla a entero
    if number:
        return int(number), matrixRef
    else:
        return -1, matrixRef



def asignaData(data,numbers):
    if(data != -1):
        if numbers[0] == -1:
            numbers[0] = data
        else:
            numbers[1] = data
    return numbers


def detectNumber(matrix, matrixRef, positionA, positionB):
    rows, cols = len(matrix), len(matrix[0])
    numbers = [-1,-1]
    # ARRIBA
    if positionA > 0:
        # diagonal izquierda
        if positionB > 0 and itsNumber(matrix[positionA - 1][positionB - 1]):
            data,matrixRef = extractNumber(matrix,matrixRef,positionA-1, positionB-1)
            numbers = asignaData(data,numbers)

        
        # arriba
        if itsNumber(matrix[positionA - 1][positionB]):
            data,matrixRef = extractNumber(matrix,matrixRef,positionA-1, positionB)
            numbers = asignaData(data,numbers)

        # diagonal derecha
        if positionB < cols - 1 and itsNumber(matrix[positionA - 1][positionB + 1]):
            data,matrixRef = extractNumber(matrix,matrixRef,positionA-1, positionB+1)
            numbers = asignaData(data,numbers)

    # LATERALES
    # izquierda
    if positionB > 0 and itsNumber(matrix[positionA][positionB - 1]):
        data,matrixRef = extractNumber(matrix,matrixRef,positionA, positionB-1)
        numbers = asignaData(data,numbers)

    # derecha
    if positionB < cols - 1 and itsNumber(matrix[positionA][positionB + 1]):
        data,matrixRef = extractNumber(matrix,matrixRef,positionA, positionB+1)
        numbers = asignaData(data,numbers)

    # ABAJO
    if positionA < rows - 1:
        # diagonal izquierda
        if positionB > 0 and itsNumber(matrix[positionA + 1][positionB - 1]):
            data,matrixRef = extractNumber(matrix,matrixRef,positionA+1, positionB-1)
            numbers = asignaData(data,numbers)

        # abajo
        if itsNumber(matrix[positionA + 1][positionB]):
            data,matrixRef = extractNumber(matrix,matrixRef,positionA+1, positionB)
            numbers = asignaData(data,numbers)

        # diagonal derecha
        if positionB < cols - 1 and itsNumber(matrix[positionA + 1][positionB + 1]):
            data,matrixRef = extractNumber(matrix,matrixRef,positionA+1, positionB+1)
            numbers = asignaData(data,numbers)

    # Si no se cumple ninguna condición, devolver False o manejar según sea necesario
    return numbers


symbolRef = "*"
configsLines = configs.split("\n")
matrixData = [list(line) for line in configsLines if line]
cloneMatrix= [[False] * len(matrixData[0]) for _ in range(len(matrixData))]
answer = 0
contador = 0

for k in range(len(matrixData)):

    for j in range(len(matrixData[k])):

        if itsSymbol(matrixData[k][j], symbolRef):
            data = detectNumber(matrixData, cloneMatrix, k, j)
            if((data[0] * data[1]) >= 0 ):
                answer += (data[0] * data[1])

print(answer)


