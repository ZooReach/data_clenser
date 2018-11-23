import pandas as pd

df=pd.read_excel('fish.xlsx')

result1 = df.rename(columns={
	'Kingdom':'kingdom',
	'Phylum':'phylum',
	'Class':'class',
	'Order':'order',
	'Family':'family',
	'Species Authority:':'species_authority',
	'Infra-specific Taxa Assessed:':'infra_specific_taxa_assessed',
	'Common Name/s: ':'common_name',
	'Synonym/s:':'synonyms',
	'Taxonomic Notes:':'taxonomic_notes',
	'Red List Category & Criteria:':'redlist_category',
	'Year Assessed:':'date_assessed',
	'Contributor/s:':'contributors',
	'Reviewer/s:':'reviewers',
	'Assessor/s:':'assessors',
	'Justification:':'justification',
	'History:':'previously_published_red_list_assessments',
	'Range Description:':'range_description',
	'Countries:':'countries_occurence',
	'FAO Marine Fishing Areas:':'fao_marine_fishing_areas',
	'Population:':'population',
	'Population Trend:':'current_population_trend',
	'Habitat and Ecology:':'habitat_and_ecology',
	'Systems:':'systems',
	'List of Habitats:':'list_of_habitats',
	'Major Threat(s):':'major_threats',
    'List of Threats:':'list_of_threats',
	'Conservation Actions:':'conservation_actions',
	'List of Conservation Actions:':'list_of_conservation_actions',
	'Bibliography:':'bibliography',
	'Citation:':'citation',
	'Endemic/Not':'endemic_status'}) 

result1['genus'] = result1['Scientific Name:'].str.split().apply(lambda x: x[0])
result1['species'] = result1['Scientific Name:'].str.split().apply(lambda x: x[1])


result1['criteria']=""
result1['year_published']=""
result1['reasons_for_change']=""
result1['regional_assessment_information']=""
result1['national_status']=""
result1['comments']=""

result1['aoo']=""
result1['eoo']=""
result1['location']=""
result1['elevation']=""
result1['range_map']=""

result1['year_of_population_estimate']=""
result1['mature_individuals']=""
result1['severely_fragmented']=""
result1['number_of_subpopulation']=""
result1['population_reduction_(gen_time)']=""
result1['generation_time']=""

result1['habit']=""
result1['niche']=""
result1['habitat_status']=""
result1['trade']=""

result1['stresses']=""

result1['presence_in_protected_areas']=""
result1['list_of_conservation_actions']=""
result1['conservation_needed']=""
result1['research_needed']=""
result1['ecosystem_services']=""


result1['endemic_status']=""


result1=result1.drop(columns=['S.No','Scientific Name:','Assessment Information [top]','Annotations:','Population [top]', 'Habitat and Ecology [top]','Threats [top]','Conservation Actions [top]','Geographic Range [top]','Map Status'])

if len(result1.columns==60):
	print "job success"


print "Thank you"