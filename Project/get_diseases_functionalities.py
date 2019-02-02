'''
retrieve diseases from uniprotkb
'''

import urllib.request
from xml.dom import minidom
from families import get_proteins_over_threshold


# GLOBAL VARIABLES
BASE_URL = 'https://www.uniprot.org/uniprot/'
EXTENSION = '.xml'

def get_diseases(proteins):
    '''
    get diseases
    INPUT: proteins list
    OUTPUT: list of diseases
    '''
    diseases = []
    for protein in proteins:
        url = BASE_URL + protein + EXTENSION
        info = urllib.request.urlopen(url).read().decode('utf-8')
        with open('./data/temp/protein.xml', 'w') as outfile:
            outfile.write(info)
        mydoc = minidom.parse('./data/temp/protein.xml')
        items = mydoc.getElementsByTagName('disease')
        if items:
            diseases.append(items[0].childNodes[1].firstChild.data)
    return diseases


def functions(proteins):
    '''
    get the function of proteins
    INPUT: protein list
    OUTPUT: list of functions
    '''
    func = []
    for protein in proteins:
        url = BASE_URL + protein + EXTENSION
        info = urllib.request.urlopen(url).read().decode('utf-8')
        with open('./data/temp/protein.xml', 'w') as outfile:
            outfile.write(info)
        mydoc = minidom.parse('./data/temp/protein.xml')
        items = mydoc.getElementsByTagName('comment')
        for item in items:
            if item.getAttribute('type') == 'function':
                func.append([protein, item.childNodes[1].firstChild.data])
    return func


def catalytic_activities(proteins):
    '''
    get the catalytic activities of proteins
    INPUT: proteins list
    OUTPUT: list of catalytic activities
    '''
    cata = []
    for protein in proteins:
        url = BASE_URL + protein + EXTENSION
        info = urllib.request.urlopen(url).read().decode('utf-8')
        with open('./data/temp/protein.xml', 'w') as outfile:
            outfile.write(info)
        mydoc = minidom.parse('./data/temp/protein.xml')
        items = mydoc.getElementsByTagName('comment')
        for item in items:
            if item.getAttribute('type') == 'catalytic activity':
                cata.append([protein, item.childNodes[1].childNodes[1].firstChild.data])
    return cata


if __name__ == "__main__":
    PROTEINS = get_proteins_over_threshold(
        './5_hmms/hmm search results/uniref90_100_90_against_homo.out', 89)
    # DISEASES = get_diseases(PROTEINS)
    # with open('./6_results/diseases.out', 'w') as out:
    #     for disease in DISEASES:
    #         out.write('{}\n'.format(disease))
    # FUNCTIONS = functions(PROTEINS)
    # with open('./6_results/functions.out', 'w') as out:
    #     for function in FUNCTIONS:
    #         out.write('{}: {}\n'.format(function[0], function[1]))
    CATALYTIC_ACTIVITIES = catalytic_activities(PROTEINS)
    with open('./6_results/catalytic_activities.out', 'w') as out:
        for cat in CATALYTIC_ACTIVITIES:
            out.write('{}: {}\n'.format(cat[0], cat[1]))
