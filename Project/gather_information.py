'''
Gather various informations for second part of the project
from uniprotkb and and MobiDB
'''

import json
import sys
import urllib.request

from families import get_proteins_over_threshold


def disorder_content(proteins):
    '''
    get disorder content from MobiDB
    '''
    with open('./6_results/disorder_content.out', 'w') as outfile:
        for protein in proteins:
            request = urllib.request.urlopen(
                "http://mobidb.bio.unipd.it/ws/{}/consensus".format(protein))
            data = json.load(request)
            outfile.write('{}: {}\n'.format(
                protein, data['mobidb_consensus']['disorder']['predictors'][1]['dc']))


def uniprot_info(proteins):
    '''
    get info from uniprot about:\n
    1)
    '''
    with open('./6_results/string.out', 'w') as outfile:
        base_url = 'https://www.uniprot.org/uniprot/'
        extension = '.txt'
        for protein in proteins:
            information = urllib.request.urlopen(
                base_url + protein + extension).read().decode('utf-8')
            for row in information.split('\n')[:-1]:
                row = row.replace(';', '')
                if row.split()[0] == 'DR':
                    if row.split()[1] == 'STRING':
                        outfile.write('{}: {}\n'.format(protein, row.split()[2]))
    with open('./6_results/kegg.out', 'w') as outfile:
        base_url = 'https://www.uniprot.org/uniprot/'
        extension = '.txt'
        for protein in proteins:
            information = urllib.request.urlopen(
                base_url + protein + extension).read().decode('utf-8')
            for row in information.split('\n')[:-1]:
                row = row.replace(';', '')
                if row.split()[0] == 'DR':
                    if row.split()[1] == 'KEGG':
                        outfile.write('{}: {}\n'.format(protein, row.split()[2]))



if __name__ == "__main__":
    PROTEINS = get_proteins_over_threshold(sys.argv[1], 89)
    disorder_content(PROTEINS)
    uniprot_info(PROTEINS)
