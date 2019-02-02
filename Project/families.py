'''
Gather all the proteins above threshold and creates a fasta file
'''

import sys
import urllib.request
import numpy as np
from precision_recall import parse_labelled_hmmout, parse_hmmout
# from blast_parser import query_uniprotkb_uniref90


def get_labelled_proteins_over_threshold(hmmout, threshold):
    '''
    get proteins from a labelled hmm output and returns
    group and family of the ones above threshold\n
    INPUT: parsed hmmout, threshold\n
    OUTPUT: list of group and families of proteins above threshold
    '''
    output = parse_labelled_hmmout(hmmout)
    proteins = np.array([])
    for row in output:
        if int(row[0]) > int(threshold):
            if proteins.size == 0:
                proteins = np.array([row[1], row[2]])
            else:
                proteins = np.vstack([proteins, [row[1], row[2]]])
    return proteins


def get_proteins_over_threshold(hmmout, threshold):
    '''
    get proteins from a hmm output and returns
    the id of the ones above threshold\n
    INPUT: parsed hmmout, threshold\n
    OUTPUT: list of ids of proteins above threshold
    '''
    output = parse_hmmout(hmmout)
    proteins = []
    for row in output:
        if int(row[0]) > int(threshold):
            proteins.append(row[1])
    return proteins


def get_pfam(proteins):
    '''
    get pfam from uniprot txt service
    '''
    base_url = 'https://www.uniprot.org/uniprot/'
    extension = '.txt'
    pfam = []
    for protein in proteins:
        information = urllib.request.urlopen(base_url + protein + extension).read().decode('utf-8')
        for row in information.split('\n')[:-1]:
            row = row.replace(';', '')
            if row.split()[0] == 'DR':
                if row.split()[1] == 'Pfam':
                    if row.split()[2] not in pfam:
                        pfam.append(row.split()[2])
    return pfam

if __name__ == "__main__":
    # PROTEINS = get_labelled_proteins_over_threshold(sys.argv[1], 89)
    PROTEINS = get_proteins_over_threshold(sys.argv[1], 89)
    PFAM = get_pfam(PROTEINS)
    with open('./6_results/pfam.out', 'w') as outfile:
        for pf in PFAM:
            outfile.write('{}\n'.format(pf))

    # query_uniprotkb_uniref90(
    #     PROTEINS, './6_results/{}.fasta'.format(sys.argv[2]), len(PROTEINS))
