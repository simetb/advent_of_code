from config import configs_1 as configs
import re

answer = 0

for data in configs.split("\n"):
    data = data[5:].split(":")
    dataInfo = data[1].replace(" ","").split(";")
    dataInfo = [dataInfo[k].split(",") for k in range(len(dataInfo))]
    bandera = True
    for grab in dataInfo:
        for cubes in grab:
            if(
                (("red" in cubes) and (int("".join(re.findall(r'\d+',cubes))) > 12)) 
               or (("green" in cubes) and (int("".join(re.findall(r'\d+',cubes))) > 13)) 
               or (("blue" in cubes) and (int("".join(re.findall(r'\d+',cubes))) > 14))
               ):
                bandera = False
    if bandera:
        answer+= int(data[0])


print(answer)




    