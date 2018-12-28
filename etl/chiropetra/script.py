import pandas as pd
from ..schema_validator import utils
import os
from itertools import chain
dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_excel(os.path.join(dir_path, 'chiropetra.xlsx'))

taxanomy = utils.taxanomy(
    family=df['Family'],
    species_authority=df['Genus + Species + Sub species + Authority'].str.split().apply(
        lambda x: ''.join(chain.from_iterable(x[2:]))),
    common_name=df['Common names'],
    synonyms=df['Synonyms'],
    # infra_specific_taxa_assessed=df['Genus + Species + Sub species + Authority'].str.split('  ').apply(lambda x: x[2]),
    genus=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[0]),
    species=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[1]))

assessment_information = utils.assessment_information(
    redlist_category=df['Ver. 3.1:'],
    criteria=df['Ver. 3.1:'],
    reviewers=df['Reviewers'],
    assessors=df['Compilers'],
    national_status=df['National Status'],
    comments=df['Comments ']
)

geographic_range = utils.geographic_range(
    range_description=df['Global'].str.cat(df['South Asia']),
    aoo=df['Area of Occupancy'],
    eoo=df['Extent of Occurrence'],

    location=df['Locations/subpopulations'].str.split('.').apply(lambda x: x[0] if isinstance(x, list) else ''),
    elevation=df['Niche'],
    countries_occurence=df['Global']
)

population = utils.population(
    mature_individuals=df['Mature individuals'],
    population=df['Population'],
    current_population_trend=df['Population trend'],
    number_of_subpopulation=df['Locations/subpopulations'].str.split('.').apply(
        lambda x: x[1] if isinstance(x, list) and len(x) > 1 else ''),
    generation_time=df['Generation time']
)

habit_and_ecology = utils.habitat_and_ecology(
    habitat_and_ecology=df['Habitat'],
    niche=df['Niche'],
    habit=df['Habit'],
    habitat_status=df['Habitat status']
)

threats = utils.threats_and_major_threats(
    threats_and_major_threats=df['Threats to the taxon']
)

conservation_actions = utils.conservation_actions(
    conservation_actions=df['Microchiroptera Action Plan (Global)'].fillna('').astype(str).str.cat(df['CITES'],
                                                                                                   sep=' CITES: ',
                                                                                                   na_rep='').str.cat(
        df['Old World Fruit Bats Action Plan (Global)'], sep=' OWFBAP: ', na_rep=''),
    presence_in_protected_areas=df['Known presence in Protected Areas'],
    conservation_needed=df['Management'].str.cat(df['Captive breeding']),
    research_needed=df['Research']
)

bibliography = utils.bibliography(
    bibliography=df['Sources'])

formed_data = [taxanomy, assessment_information, geographic_range, population, habit_and_ecology, threats,
               conservation_actions, bibliography]

utils.validate_print_result(formed_data=formed_data, num_rows=33, path=dir_path)
