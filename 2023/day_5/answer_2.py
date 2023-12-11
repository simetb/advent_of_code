from config import configs_2 as configs


def itsNumber(character):
    try:
        int(character)
        return True
    except:
        return False

def processData(config):

    config = [data for data in config.split("\n") if data != '']

    firstConf = config[0] 
    pIndice = firstConf.index(":") + 2
    config[0] = firstConf[pIndice:]

    outpuConfig = []
    temporalConfig = []

    for configProcess in config:
        if(itsNumber(configProcess[0])):
            temporalConfig.append(configProcess)
        else:
            outpuConfig.append(temporalConfig)
            temporalConfig = []

    outpuConfig.append(temporalConfig)
    return outpuConfig

def searchMap(mapa,number):
    
    answer = -1
    for data in mapa:
        data = [int(value) for value in data.split(" ")]

        i = data[1]
        s = data[2]
        d = data[0]
        l = (s - 1) + i
                 
        if(i <= number and number <= l):
            si = abs(number - i)
            sa = abs(si + d)
            answer = sa       
    
    if answer == -1:
        answer = number
    
    return answer

config = processData(configs)
locations = []
answer = 0
seedRanges = config[0][0].split(" ")
seedRangesConfig = [
    [int(seedRanges[int(k) - 2]),int(seedRanges[int(k) - 1])] for k in range(2, len(seedRanges)+2, 2)
]


seedTest = []
for seedConfig in  seedRangesConfig:

    seed_min_range = seedConfig[0]
    seed_max_range = seedConfig[0] - (seedConfig[1]-1)

    for soilConfig in config[1]:
        
        soilConfig = [int(data) for data in soilConfig.split(" ")]
        destConf, minConf, rangeConf = soilConfig
        maxConf = minConf + rangeConf

        if(seed_min_range >= minConf and seed_max_range <= maxConf):
            
            print(soilConfig)










    for seed in range(seedConfig[0], seedConfig[0] + seedConfig[1]):
        
        seed = int(seed)
        # Seed 
        # print(seed)
        
        # Soil    
        answer = searchMap(config[1],seed)
        # print(f"Soil: {answer}")
        
        # # Fertilizer
        answer = searchMap(config[2],answer)
        # print(f"Fertilizer: {answer}")
        
        # # Water
        answer = searchMap(config[3],answer)
        # print(f"Water: {answer}")
        
        # # Light
        answer = searchMap(config[4],answer)
        # print(f"Light: {answer}")
        
        # # Temperature
        answer = searchMap(config[5],answer)
        # print(f"Temperature: {answer}")
        
        # # Humidity
        answer = searchMap(config[6],answer)
        # print(f"Humidity: {answer}")
        
        # # Location
        answer = searchMap(config[7],answer)
        # print(f"Location: {answer}")
        
        seedTest.append(f"{seedConfig[0]} - {seedConfig[1]}, {seed}")
        locations.append(answer)
        
        # print("\n")

ind = locations.index(min(locations))



print(locations[ind])
print(seedTest[ind])

# print(min(locations)) 