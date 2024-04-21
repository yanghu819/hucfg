

hucfg = {}
hucfg['lr'] = [0.1,0.2]
hucfg['wd'] = [0.05, 0.005]
hucfg['shape'] = [224, 336]
source_folder = 'exp##0'
target_base_name = source_folder + ','


import os
import shutil
import itertools
import re
import json
keys, values = zip(*hucfg.items())
combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

param_list = {}

for n in range(len(combinations)):  
    target_folder = f'copy-{target_base_name}{n+1}'
    param_list[str(re.search(r'##(.*)', target_folder).group(1))] = combinations[n]
    if not os.path.exists(target_folder):
        shutil.copytree(source_folder, target_folder)
    else:
        print(f'{target_folder} already exists')
        
## exp##0 has the last setting
param_list[str(re.search(r'##(.*)', source_folder).group(1))] = combinations[n]  

hucfg_path = './hucfg.json'

with open(hucfg_path, 'w') as file:
    json.dump(param_list, file, indent=4)

