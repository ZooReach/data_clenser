import pandas as pd
from ..schema_validator import utils
import os

dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_excel(os.path.join(dir_path, 'primates.xlsx'))
taxanomy = utils.taxanomy(
    # kingdom=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[0]),
    # phylum=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[1]),
    # class_name=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[2]),
    # order=df['Order'],
    family=df['Family'],
    species_authority=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[3]),
    # infra_specific_taxa_assessed=df['Infra-specific Taxa Assessed: '],
    common_name=df['Common names'],
    synonyms=df['Synonyms'],
    taxonomic_notes=df['Notes on taxonomy'],
    genus=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[0]),
    species=df['Genus + Species + Sub species + Authority'].str.split().apply(lambda x: x[1]))

assessment_information = utils.assessment_information(
    redlist_category=df['2001 Red List (Ver. 2.3)'],
    # date_assessed=df['Year Assessed:'],
    contributers=df['Compilers'],
    reviewers=df['Reviewers'],
    # assessors=df['Assessor/s:'],
    justification=df['Justification for change'],
    national_status=df['National Status'],
    comments=df['Comments'])

geographic_range = utils.geographic_range(
    # range_description=df['Range Description:'],
    # countries_occurence=df['Countries:'],
    endemic_status=df['Endemic status (Regional)'],
    elevation=df['Elevation'])

population = utils.population(
    population=df['Population'],
    current_population_trend=df['Population trend'],
    generation_time=df['Generation time'],
    mature_individuals=df['Mature individuals'],
)

habit_and_ecology = utils.habitat_and_ecology(
    habitat_and_ecology=df['Habitat'],
    habit=df['Habit'],
    niche=df['Niche'],
    # systems=df['Systems:'],
    # list_of_habitats=df['List of Habitats:']
)

threats = utils.threats_and_major_threats(
    threats_and_major_threats=df['Threats'],
    # list_of_threats=df['List of Threats:']
)

conservation_actions = utils.conservation_actions(
    presence_in_protected_areas=df['Presence in Protected Areas                                        '],
    research_needed=df['Research'])

bibliography = utils.bibliography(
    # bibliography=df['Bibliography [top]']
)

citation = utils.citation(
    citation=df['Sources'])

formed_data = [taxanomy, assessment_information, geographic_range, population, habit_and_ecology, threats,
               conservation_actions, bibliography, citation]

utils.validate_print_result(formed_data=formed_data, num_rows=26, path=dir_path)
