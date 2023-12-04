from config import configs_2 as configs

gamesGuessed =  [0] * len(configs.split("\n"))
gamesScratches = [1] * len(configs.split("\n"))
configs = configs.split("\n")

for Indexconfig in range(len(configs)):
    # Processing data
    configColon = configs[Indexconfig].index(":") + 1

    # Extranctin ":"
    config = configs[Indexconfig][configColon:]

    # Getting the results
    winnigResults, gessResults = config.split("|")

    # Processing the results
    winnigResults = winnigResults.split(" ")
    winnigResults = [num for num in winnigResults if num != '']

    gessResults = gessResults.split(" ")
    gessResults = [num for num in gessResults if num != '']

    gessed = 0
    for wr in winnigResults:
        for gr in gessResults:
            if(wr == gr):
                gessed+=1
    
    gamesGuessed[Indexconfig] = gessed

for k in range(len(gamesGuessed)):

    for j in range(int(gamesGuessed[k])):
        give = gamesScratches[k]
        if (1+k+j) <=  len(gamesScratches):
            gamesScratches[1+k+j] += give
        else:
            pass

answer = 0
for plus in  gamesScratches:
    answer +=  int(plus)  

print(answer) 