from config import configs_1 as configs


def itsNumber(data):
    try:
        int(data)
        return True
    except:
        return False

def separateData(configs):

    data = configs.split("\n")
    # Seeds
    data[0] = data[0][data[0].index(":") + 2:]

    # Other data
    # seed-to-soil map
    # soil-to-fertilizer map:
    # fertilizer-to-water map:
    # water-to-light map:
    # light-to-temperature map:
    # temperature-to-humidity map:
    # humidity-to-location map:

    skip = False
    newArrayData = []
    for dataA in data:
        if(skip):
            if(dataA != ""):
                print(itsNumber(dataA[0]))
        else: 
            skip = True

    print(data)


separateData(configs)

    