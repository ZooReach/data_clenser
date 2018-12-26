import pandas as pd
from ..schema_validator import utils
import os

dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_excel(os.path.join(dir_path, 'molluscs.xlsx'))
taxanomy = utils.taxanomy(
    kingdom=df['Kingdom'],
    phylum=df['Phylum'],
    class_name=df['Class'],
    order=df['Order'],
    family=df['Family'],
    species_authority=df['Species Authority:'],
    infra_specific_taxa_assessed=df['Infra-specific Taxa Assessed: '],
    common_name=df['Common Name/s:'],
    synonyms=df['Synonyms'],
    taxonomic_notes=df['Taxonomic Notes:'],
    genus=df['Scientific Name:'].str.split().apply(lambda x: x[0]),
    species=df['Scientific Name:'].str.split().apply(lambda x: x[1]))

assessment_information = utils.assessment_information(
    redlist_category=df['Red List Category & Criteria:'],
    date_assessed=df['Year Assessed:'],
    contributers=df['Contributors'],
    reviewers=df['Reviewer/s:'],
    assessors=df['Assessor/s:'],
    justification=df['Justification:'],
    previously_published_red_list_assessments=df['History'])

geographic_range = utils.geographic_range(
    range_description=df['Range Description:'],
    countries_occurence=df['Countries:'])

population = utils.population(
    population=df['Population:'],
    current_population_trend=df['Population Trend:'])

habit_and_ecology = utils.habitat_and_ecology(
    habitat_and_ecology=df['Habitat and Ecology:'],
    systems=df['Systems:'],
    list_of_habitats=df['List of Habitats:'])

threats = utils.threats_and_major_threats(
    threats_and_major_threats=df['Major Threat(s):'],
    list_of_threats=df['List of Threats:'])

conservation_actions = utils.conservation_actions(
    conservation_actions=df['Conservation Actions:'],
    list_of_conservation_actions=df['List of Conservation Actions:'])

bibliography = utils.bibliography(
    bibliography=df['Bibliography [top]'])

citation = utils.citation(
    citation=df['Citation:'])

formed_data = [taxanomy, assessment_information, geographic_range, population, habit_and_ecology, threats,
               conservation_actions, bibliography, citation]

utils.validate_print_result(formed_data=formed_data, num_rows=32, path=dir_path)
