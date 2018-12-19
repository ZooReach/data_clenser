import pandas as pd
from ..schema_validator import utils
import os

dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(dir_path, 'result.csv'))

data = {
'Eels' : {'Anguillidae':'Freshwater Eels','Ophichthidae':'Snake Eels','Mastacembelidae':'Spiny Eel',
              'Synbranchidae':'Swamp Eel','Chaudhuridae':'Earthworm Eel'},

'Rice Fish' : {'Adrianichthyidae':'Rice Fish'},

'Spipe Fish' : {'Hemiramphidae':'Spipe Fish'},

'Needle Fish' : {'Belonidae':'Needlefish'},

'Ray Finned Fish' : {'Clupeidae':'Ray-finned fish'},

'Loaches' : {'Balitoridae':'Hillstream Loach','Cobitidae':'True Loaches'},

'Carps Minnows' : {'Cyprinidae':'Carps & Truw Minnow','Psilorhynchidae':'Torrent Minnow'},

'Panchax Fish' : {'Aplocheilidae':'Panchax fish'},

'Featherback & Knifefishes' : {'Notopteridae':'Featheback & Knifefish'},

'Perches' : {'Ambassidae':'Perchlet','Anabantidae':'Climbing Perch','Terapontidae':'Tiger Perch'},

'Tiger Perch': {'Channidae':'Snakehead'},

'Cichlid': {'Cichlidae ':'Cichlid'},

'Gobies': {'Eleotridae':'Sleeper Gobies','Gobiidae':'True Gobies'},

'Leaffish':{'Nandidae':'Asian Leaffish'},

'Gourami':{'Osphronemidae':'Gourami'},

'Catfishes': { 'Erethistidae' : 'Erethestid Catfish',
              'Heteropneustidae':'Air-sac Catfish',
              'Pangasiidae' : 'Shark Catfish',
              'Shark Catfis':'Schilbid Catfish',
              'Siluridae':'Silurid Catfish',
              'Sisoridae' : 'Sisorid Catfish',
              'Bagridae' :'Naked Catfish',
             'Clariidae' :'Air-breathing Catfish',
              'Amblycipitidae':'Torrent Catfish',
              'Arridae':'Ariid Catfish',
              'Chacidae':'Squarehead Catfish',
              'Akysidae':'Stream Catfish',
              'Olyridae':'Longtail Catfish'
              },

'Pipefish': {'Syngnathidae':'Pipefish'},

'Puffer Fish': {'Tetraodontidae':'Puffer fish'},

'Anchovy': {'Engraulidae':'Anchovy'},

'Herring': {'Pristigasteridae':'Longfin Herring'},

'Stickleback': {'Indostomidae':'Armored Stickleback'},

'Mullet': {'Mugilidae':'Mullet'},

'Chameleonfish':{'Badidae':'Chameleonfish'},

 'Stingrays' : {'Dasyatidae':'Whiptail Stingray'},

}

for hierarchy in data.keys():
    group_level_data = data[hierarchy]
    for familyName in group_level_data.keys():
        df.loc[df["family"].str.upper() == familyName.upper(), "category_level1"] = hierarchy
        df.loc[df["family"].str.upper() == familyName.upper(), "category_level2"] = group_level_data[familyName]

df.to_csv("test.csv",  encoding='utf-8', index=False)
