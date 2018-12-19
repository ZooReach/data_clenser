import pandas as pd
from collections import namedtuple

from itertools import chain
import functools
import os

taxanomy_fields = ('kingdom',
                   'phylum',
                   'class_name',
                   'order',
                   'family',
                   'genus',
                   'species',
                   'species_authority',
                   'infra_specific_taxa_assessed',
                   'common_name',
                   'synonyms',
                   'taxonomic_notes')

assessment_information_fields = ('redlist_category',
                                 'criteria',
                                 'date_assessed',
                                 'year_published',
                                 'contributers',
                                 'reviewers',
                                 'assessors',
                                 'justification',
                                 'previously_published_red_list_assessments',
                                 'reasons_for_change',
                                 'regional_assessment_information',
                                 'national_status',
                                 'comments')

geographic_range_fields = ('range_description',
                           'aoo',
                           'eoo',
                           'location',
                           'elevation',
                           'countries_occurence',
                           'range_map',
                           'fao_marine_fishing_areas',
                           'endemic_status')

population_fields = ('population',
                     'current_population_trend',
                     'year_of_population_estimate',
                     'mature_individuals',
                     'severely_fragmented',
                     'number_of_subpopulation',
                     'population_reduction_gen_time',
                     'generation_time')

habitat_and_ecology_fields = ('habitat_and_ecology',
                              'systems',
                              'list_of_habitats',
                              'habit',
                              'niche',
                              'habitat_status')

threats_and_major_threats_fields = ('threats_and_major_threats',
                                    'list_of_threats',
                                    'trade')

stresses_fields = ('stresses',)

conservation_actions_fields = ('conservation_actions',
                               'presence_in_protected_areas',
                               'list_of_conservation_actions',
                               'conservation_needed',
                               'research_needed',
                               'ecosystem_services')

bibliography_fields = ('bibliography',)
citation_fields = ('citation',)

category_level_fields = ('category_level1','category_level2')

taxanomy = namedtuple('taxanomy', taxanomy_fields, defaults=(None,) * len(taxanomy_fields), rename=True)
assessment_information = namedtuple('assessment_information', assessment_information_fields,
                                    defaults=(None,) * len(assessment_information_fields))
geographic_range = namedtuple('geographic_range', geographic_range_fields,
                              defaults=(None,) * len(geographic_range_fields))
population = namedtuple('population', population_fields, defaults=(None,) * len(population_fields))
habitat_and_ecology = namedtuple('habitat_and_ecology', habitat_and_ecology_fields,
                                 defaults=(None,) * len(habitat_and_ecology_fields))
threats_and_major_threats = namedtuple('threats_and_major_threats', threats_and_major_threats_fields,
                                       defaults=(None,) * len(threats_and_major_threats_fields))
stresses = namedtuple('stresses', stresses_fields, defaults=(None,) * len(stresses_fields))
conservation_actions = namedtuple('conservation_actions', conservation_actions_fields,
                                  defaults=(None,) * len(conservation_actions_fields))
bibliography = namedtuple('bibliography', bibliography_fields, defaults=(None,) * len(bibliography_fields))
citation = namedtuple('citation', citation_fields, defaults=(None,) * len(citation_fields))
category_level = namedtuple('category_level',category_level_fields, defaults=(None,) * len(category_level_fields))

first_level_header = [taxanomy, assessment_information, geographic_range, population, habitat_and_ecology,
                      threats_and_major_threats, stresses, conservation_actions, bibliography,category_level]


def validate_dataframe(named_tuples, num):
    count = functools.reduce(lambda x, y: x + y,
                             chain.from_iterable(
                                 map(lambda header:
                                     map(lambda field: int(getattr(header, field) is not None),
                                         header._fields), named_tuples)))

    print("validation ", "passed" if count == num else "failed", " with ", count)

    return count == num


def form_data_frame(named_tuples):
    column_header = list(chain.from_iterable(
        map(lambda fields: fields, map(lambda header: map(lambda field: field, header._fields), first_level_header))))
    df = pd.DataFrame(columns=column_header)
    for header in named_tuples:
        for field in header._fields:
            if getattr(header, field) is None:
                df[field] = ""
            else:
                df[field] = getattr(header, field)

    return df


def validate_print_result(formed_data, num_rows, path):
    return form_data_frame(formed_data).to_csv(os.path.join(path, "result.csv"), encoding='utf-8',
                                               index=False) if validate_dataframe(formed_data, num_rows) else "error"
