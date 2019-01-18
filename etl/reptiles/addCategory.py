
import pandas as pd
import os
import json


dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(dir_path, 'result.csv'))

data = {}
with open(os.path.join(dir_path, 'schema.json')) as f:
    data = json.load(f)


for hierarchy in data.keys():
    group_level_data = data[hierarchy]
    for familyName in group_level_data.keys():
        df.loc[df["genus             "].str.strip().str.upper() == familyName.upper(), "category_level1"] = hierarchy
        df.loc[df["genus             "].str.strip().str.upper() == familyName.upper(), "category_level2"] = \
        group_level_data[
            familyName]
df.to_csv("test.csv", encoding='utf-8', index=False)
