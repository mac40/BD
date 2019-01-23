'''
Transform the xml output of a blast query into a fasta file containing the proteins from uniprotkb\n
INPUT: xml file containing blast output\n
OUTPUT: fasta file containing proteins matched by blast\n
'''

import os
# import sys
import urllib.request
import xml.etree.ElementTree as ET

FILE_POS = os.path.dirname(os.path.abspath(__file__))


def xml_to_protein_list(xml_file):
    '''
    parse blast\n
    INPUT: xml_file_name\n
    RETURN: list of proteins\n
    '''
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for sssr in root.findall('{http://www.ebi.ac.uk/schema}SequenceSimilaritySearchResult'):
        for hits in sssr:
            hit_list = []
            for hit in hits:
                protein = hit.get('ac')
                if protein not in hit_list:
                    hit_list.append(protein)
    return hit_list


def txt_to_protein_list(txt_file):
    '''
    parse txt\n
    INPUT: txt_file\n
    RETURN: list of proteins
    '''
    hit_list = []
    with open(txt_file, 'r') as infile:
        for protein in infile:
            if protein not in hit_list:
                hit_list.append(protein[:-1])
    return hit_list


def query_uniprotkb_uniref90(proteins, output_file_name, number):
    '''
    query uniprotkb for sequences given a protein list and output them in a fasta file\n
    INPUT: protein list, name of output file, number of proteins to use\n
    OUTPUT: fasta file with proteins sequences\n
    '''
    with open(output_file_name, 'w') as output:
        base_url = 'https://www.uniprot.org/uniprot/'
        upi_url = 'https://www.uniprot.org/uniparc/'
        extention = '.fasta'
        for protein in range(0, number):
            if proteins[protein][:3] == 'UPI':
                url = upi_url + proteins[protein] + extention
                protein_fasta = urllib.request.urlopen(url).read()
                output.write(protein_fasta.decode("utf-8"))
            else:
                url = base_url + proteins[protein] + extention
                protein_fasta = urllib.request.urlopen(url).read()
                output.write(protein_fasta.decode("utf-8"))


if __name__ == "__main__":
    pass
    # if len(sys.argv) == 1:
    #     print('no parameters specified (type python blast_parser.py -h for help)')
    #     sys.exit()
    # elif str(sys.argv[1]) == '-h':
    #     print('python blast_parser.py xml_file output_file_name')
    #     sys.exit()
    # elif len(sys.argv) < 3:
    #     print('missing parameters')
    #     sys.exit()
    # else:
    #     PROTEIN_LIST = xml_to_protein_list(sys.argv[1])
    #     query_uniprotkb(PROTEIN_LIST,
    #                     '{}/parsed_blast_results/{}.fasta'.format(
    #                         FILE_POS, sys.argv[2]),
    #                     100)
