import pandas as pd
import os
import json

dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_excel(os.path.join(dir_path, 'reptile_schema.xlsx'))

dict = df.to_dict()

result = {}
length = len(dict['Hierarchy Level 1'].values())
for i in range(0, length):
    l1 = list(dict['Hierarchy Level 1'].values())[i]
    l2 = list(dict['Hierarchy Level 2'].values())[i]
    family = list(dict['Family'].values())[i]
    genus = family.split(' ')[1][1:-1]

    val = {genus: l2}

    if l1 in result.keys():
        data = result[l1]
    else:
        data = {}

    data.update(val)

    result.update({l1: data})

with open(os.path.join(dir_path, 'schema.json'), 'w') as outfile:
    json.dump(result, outfile)
