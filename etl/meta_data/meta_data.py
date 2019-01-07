import pandas as pd

import os
import json
dir_path = os.path.join(os.path.dirname(__file__))
data_dir = os.path.join(os.path.abspath(os.path.join(dir_path, os.pardir)),'data')

#files= ["fishes.json"]


def readSpecies_json():
    result = {}
    files = readFileNames()
    for file in files:
        data = readJsonFile(os.path.join(data_dir,file))
        speciesKey = list(data['type'].keys())[0]
        speciesData = data['type'][speciesKey]
        commonName = speciesData['Name']
        resourceid = speciesData['resource_id']
        categories_dict = {}
        species_detail = {'resoruce_id':resourceid}
        if 'type' in speciesData.keys():
            category_level1_types = speciesData['type']
            for level1_species_name in category_level1_types:
                if 'type' in category_level1_types[level1_species_name].keys():
                    category_level2_types = category_level1_types[level1_species_name]['type']
                    species_list = list(category_level2_types.keys())
                    categories_dict[level1_species_name] = species_list
        species_detail['categories'] = categories_dict
        result[commonName] = species_detail
    return result


def readJsonFile(file):
    with open(file) as f:
        return json.load(f)


def readFileNames():
    return [item for item in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, item))]


def writeMetaData(speciesAndCategories={}):
    name = []
    parent_ids = []
    ids = []
    resourceids = []
    id = 0
    grand_parent_id = 0
    for species in speciesAndCategories.keys():
        name.append(species)
        parent_ids.append(grand_parent_id)
        id = id +1
        ids.append(id)
        parent_id = id;
        resoruce_id = speciesAndCategories[species]['resoruce_id']
        resourceids.append('')
        categories_dict = speciesAndCategories[species]['categories']

        for categories_level1 in categories_dict.keys():
            id = id + 1
            ids.append(id)
            resourceids.append('')
            name.append(categories_level1)
            parent_ids.append(parent_id)
            level1_parent_id = id
            categories_level2_species = set(categories_dict[categories_level1])
            for categories_level2 in categories_level2_species:
                id = id+1
                ids.append(id)
                resourceids.append(resoruce_id)
                name.append(categories_level2)
                parent_ids.append(level1_parent_id)

    images = ['images/placeholder.svg'] * len(ids)
    df = pd.DataFrame({'id':ids,'name':name,'parent_id':parent_ids,'image':images,'resource_id':resourceids})
    df.to_csv(os.path.join(dir_path, "metadata.csv"), encoding='utf-8',index=False)

    
if __name__ == '__main__':
    speciesAndCategories = readSpecies_json()
    writeMetaData(speciesAndCategories)


