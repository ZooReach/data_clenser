import pandas as pd
from ..schema_validator import utils
import os

dir_path = os.path.join(os.path.dirname(__file__))
df = pd.read_excel(os.path.join(dir_path, 'reptiles.xlsx'), sheet_name="WG_reptile_tds")

taxanomy = utils.taxanomy(
    kingdom=df['Kingdom'],
    phylum=df['Phylum'],
    class_name=df['Class'],
    order=df['Order'],
    family=df['Family'],
    species_authority=df['Species_Authority'],
    common_name=df['Common_Name'],
    synonyms=df['synonyms'],
    taxonomic_notes=df['Taxonomic_Notes'],
    genus=df['Genus'],
    species=df['Species'])

assessment_information = utils.assessment_information(
    redlist_category=df['Red_List_Category & Criteria'],
    date_assessed=df['Date_Assessed'],
    year_published=df['Year_Published'],
    contributers=df['Contributor/s'],
    reviewers=df['Reviewer/s'],
    assessors=df['Assessor/s'],
    justification=df['Justification'],
    comments=df['Comments']
)

geographic_range = utils.geographic_range(
    range_description=df['Range_Description'],
    countries_occurence=df['Countries'],
    range_map=df['Range_Map']
)

population = utils.population(
    population=df['Population'],
    current_population_trend=df['Population_Trend'])

habit_and_ecology = utils.habitat_and_ecology(
    habitat_and_ecology=df['Habitat and Ecology'],
    systems=df['Systems']
)

threats = utils.threats_and_major_threats(
    threats_and_major_threats=df['Major_Threats'])

conservation_actions = utils.conservation_actions(
    conservation_actions=df['Conservation_Actions'])

bibliography = utils.bibliography(
    bibliography=df['Bibliography'])

citation = utils.citation(
    citation=df['Citation'])

formed_data = [taxanomy, assessment_information, geographic_range, population, habit_and_ecology, threats,
               conservation_actions, bibliography, citation]

utils.validate_print_result(formed_data=formed_data, num_rows=30, path=dir_path)
