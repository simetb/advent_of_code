from config import configs_1 as configs
import re
total = 0
for dataConfig in configs.split():
    total += int(re.search(r'\d+',dataConfig[::1]).group()[0] + 
                 re.search(r'\d+',dataConfig[::-1]).group()[0])
print(total)