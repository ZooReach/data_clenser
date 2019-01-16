import pandas as pd
from ..schema_validator import utils
import os

dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(dir_path, 'result.csv'))

data = {
    'Fruit Bat': {
        'Cynopterus': 'Short-nosed Fruit Bat',
        'Eonycteris': 'Dawn Bat',
        'Latidens': 'Wide-toothed Bat',
        'Macroglossus': 'Long-nosed Fruit Bat',
        'Megaerops': 'Tailless Fruit Bat',
        'Pteropus': 'Flying Fox',
        'Rousettus': 'Rosy Bat',
        'Sphaerias': 'Round-nosed Bat'
    },
    'Insect Bat': {
        'Rhinolophus': 'Horseshoe Bat',
        'Hipposideros': 'Leaf-nosed Bat',
        'Asellia': 'Trident Leaf-nosed Bat',
        'Coelops': 'Tailless Leaf-nosed Bat',
        'Triaenops': 'Trident Bat',
        'Megaderma': 'False Vampire Bat',
        'Rhinopoma': 'Mouse-tailed Bat',
        'Saccolaimus': 'Pouched Bat',
        'Taphozous': 'Tomb Bat',
        'Tadarida': 'Free-tailed Bat',
        'Cherephon': 'Mastiff Bat',
        'Otomopos': 'Mastiff Bat',
        'Arielulus': 'Sprites',
        'Eptesicus': 'Serotines',
        'Hesperoptenus': 'False Serotines',
        'Scotoecus': 'Yellow Bat',
        'Scotomanes': 'Harlequin Bat',
        'Scotophilus': 'Yellow House Bat',
        'Nyctalus': 'Noctules',
        'Pipistrellus, Scotozous, Hypsugo': 'Pipistrelles',
        'Barbastella': 'Barbastelles',
        'Plecotus, Otonycteris': 'Long-eared Bat',
        'Falsistrellus': 'False Pipistrelles',
        'Ia': 'Evening Bat',
        'Philetor': 'Philetor Bat',
        'Tylonycteris': 'Bamboo Bat',
        'Vespertilio': 'Parti-coloured Bat',
        'Myotis': 'Mouse-eared Bat',
        'Harpiocephalus': 'Hairy-winged Bat',
        'Murina, Harpiola': 'Tube-nosed Bat',
        'Kerivoula': 'Woolly Bat',
        'Miniopterus': 'Long-fingered Bat'
    }

}

for hierarchy in data.keys():
    group_level_data = data[hierarchy]
    for familyName in group_level_data.keys():
        df.loc[df["genus         "].str.strip().str.upper() == familyName.upper(), "category_level1"] = hierarchy
        df.loc[df["genus         "].str.strip().str.upper() == familyName.upper(), "category_level2"] = \
        group_level_data[familyName]

df.to_csv(os.path.join(dir_path, "test.csv"), encoding='utf-8', index=False)
