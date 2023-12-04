from config import configs_1 as configs

def detectNumber(data):
    try:
        if(type(int(data)) == int):
            return True
    except:
        return False
    
def detectAdyacentSymbol(top,mid,bot,index,configsData):

    symbolArray = getSymbolsIndex(top, mid, bot, configsData[0])
    bandera = False
    for symbolArrayIndex in range(len(symbolArray)):
        if symbolArray[symbolArrayIndex] == 1:
            limInf = (index[0] - 1) if index[0] != 0 else 0
            limSup = (index[1] + 1) if index[1] != configsData[0] else configsData[0]

            if symbolArrayIndex >= limInf and symbolArrayIndex <= limSup:
                bandera = True
                break
    return bandera

def getSymbolsIndex(topSymbols,midSymbols,botSymbols,length):
    symbolIndexArray = [0 for x in range(length)]
    for indexSymbol in range(length):
        
        if(topSymbols != ''):
            if((not detectNumber(topSymbols[indexSymbol])) and 
            (topSymbols[indexSymbol] != ".")):
                symbolIndexArray[indexSymbol] = 1
        
        if(botSymbols != ''):
            if((not detectNumber(botSymbols[indexSymbol])) and 
            (botSymbols[indexSymbol] != ".")):
                symbolIndexArray[indexSymbol] = 1
        
        if(midSymbols != ''):
            if((not detectNumber(midSymbols[indexSymbol])) and 
            (midSymbols[indexSymbol] != ".")):
                symbolIndexArray[indexSymbol] = 1
    return symbolIndexArray

data = configs.split("\n")
dataConfigs = [len(data[0]) - 1, len(data) - 1] 
firstLastIndex = [-1,-1]
firstIndexBool = True
answer = 0
number = ""

# Data separada
for indexData in range(len(data)):
    firstIndexBool = True
    number = ""
    firstLastIndex = [-1,-1]

    for index in range(len(data[indexData])):
        if(detectNumber(data[indexData][index])):
            if(firstIndexBool):
                firstLastIndex[0] = index;
                firstIndexBool = False
            number+= data[indexData][index]
        
        else:
            if(not firstIndexBool):
                firstLastIndex[1] = index - 1
                firstIndexBool = True
                if(detectAdyacentSymbol(
                    data[indexData -1 ]  if indexData > 0 else "",
                    data[indexData],
                    data[indexData + 1]  if indexData < dataConfigs[1] else "",
                    firstLastIndex,
                    dataConfigs
                )):
                    answer += int(number)
                else:
                    pass
                number = ""
                firstLastIndex = [-1,-1]

print(answer) 

            






    