from config import configs_2 as configs
import re

def dataConverter(data,numbers,digits):

    word = ""
    for k in range(0,len(data)):
        word += data[k:k+1]
        for j in range(len(numbers)):
            if(numbers[j] in word):
                word = word.replace(numbers[j],digits[j])
    return word


numbers = ["one","two","three","four","five","six","seven","eight","nine"]
digits = ["1","2","3","4","5","6","7","8","9"]
answer = 0

for dataConfig in configs.split():
    firstProcessData = "".join(re.findall(r'\d+',dataConverter(
        dataConfig,
        numbers,
        digits
    )))
    secondProcessData = "".join(re.findall(r'\d+',dataConverter(
        dataConfig[::-1],
        [number[::-1] for number in numbers],
        digits
    )))
    answer += int(firstProcessData[0] + secondProcessData[0])

print(answer)