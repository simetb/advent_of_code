from config import configs_1 as configs

answer = 0
for config in configs.split("\n"):
    # Processing data
    configColon = config.index(":") + 1

    # Extranctin ":"
    config = config[configColon:]

    # Getting the results
    winnigResults, gessResults = config.split("|")

    # Processing the results
    winnigResults = winnigResults.split(" ")
    winnigResults = [num for num in winnigResults if num != '']

    gessResults = gessResults.split(" ")
    gessResults = [num for num in gessResults if num != '']

    counter = 0
    for wr in winnigResults:
        for gr in gessResults:
            if(wr == gr):
                counter+=1
    
    if(counter == 1):
        answer += 1
    elif(counter == 2):
        answer +=2
    elif(counter >= 3):
        answer += (2 ** (counter - 1))

print(answer)



    