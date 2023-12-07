from config import configs_1 as configs


def itsNumber(data):
    try:
        int(data)
        return True
    except:
        return False

def itsSymbol(data):
    if(not(itsNumber(data)) and data != "."):
        return True
    return False

def detectSymbol(matrix, positionA, positionB):
    rows, cols = len(matrix), len(matrix[0])

    # ARRIBA
    if positionA > 0:
        # diagonal izquierda
        if positionB > 0 and itsSymbol(matrix[positionA - 1][positionB - 1]):
            return True
        
        # arriba
        if itsSymbol(matrix[positionA - 1][positionB]):
            return True

        # diagonal derecha
        if positionB < cols - 1 and itsSymbol(matrix[positionA - 1][positionB + 1]):
            return True

    # LATERALES
    # izquierda
    if positionB > 0 and itsSymbol(matrix[positionA][positionB - 1]):
        return True

    # derecha
    if positionB < cols - 1 and itsSymbol(matrix[positionA][positionB + 1]):
        return True

    # ABAJO
    if positionA < rows - 1:
        # diagonal izquierda
        if positionB > 0 and itsSymbol(matrix[positionA + 1][positionB - 1]):
            return True

        # abajo
        if itsSymbol(matrix[positionA + 1][positionB]):
            return True

        # diagonal derecha
        if positionB < cols - 1 and itsSymbol(matrix[positionA + 1][positionB + 1]):
            return True

    # Si no se cumple ninguna condición, devolver False o manejar según sea necesario
    return False


configsLines = configs.split("\n")
matrixData = [list(line) for line in configsLines if line]
number = ""
answer = 0
simbol = False

for k in range(len(matrixData)):

    for j in range(len(matrixData[k])):

        if(itsNumber(matrixData[k][j])):
            number += matrixData[k][j]
            if(detectSymbol(matrixData,k,j)):
                simbol = True
        else:
            if(simbol):
                answer += int(number)
                simbol = False
            
            number = ""

print(answer)