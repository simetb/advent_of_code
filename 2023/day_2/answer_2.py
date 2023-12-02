from config import configs_2 as configs
import re

# red = 0
# green = 1
# blue = 2
asnwerSum = 0

for data in configs.split("\n"):
    data = data[5:].split(":")
    dataInfo = data[1].replace(" ","").split(";")
    dataInfo = [dataInfo[k].split(",") for k in range(len(dataInfo))]
    answerMult = 1
    select = [1,1,1]
    for grab in dataInfo:
        for cubes in grab:
            number = int("".join(re.findall(r'\d+',cubes)))
            if(("red" in cubes) and (select[0] < number)):
                select[0] = number
            if(("green" in cubes) and (select[1] < number)):
                select[1] = number
            if(("blue" in cubes) and (select[2] < number)):
                select[2] = number

    for cube in select: answerMult *= cube
    asnwerSum+=answerMult

print(asnwerSum)





    