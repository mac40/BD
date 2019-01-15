'''
Transform the xml output of a blast query into a fasta file containing the proteins from uniprotkb
INPUT: xml file containing blast output
OUTPUT: fasta file containing proteins matched by blast
'''

import urllib.request
import xml.etree.ElementTree as ET


def parse_blast(xml_file, output_file_name):
    '''
    parse blast
    INPUT: xml_file_name, outputfilename
    OUTPUT: fasta file
    '''
    tree = ET.parse(xml_file)
    root = tree.getroot()
    base_url = "https://www.uniprot.org/uniprot/"
    extention = ".fasta"
    with open(output_file_name, "w") as output:
        for sssr in root.findall('{http://www.ebi.ac.uk/schema}SequenceSimilaritySearchResult'):
            for hits in sssr:
                hit_list = []
                for hit in hits:
                    protein = hit.get('ac')
                    if protein not in hit_list:
                        hit_list.append(protein)
                        url = base_url + protein + extention
                        protein_fasta = urllib.request.urlopen(url).read()
                        output.write(protein_fasta.decode("utf-8"))


if __name__ == "__main__":
    parse_blast('ncbiblast-R20190112-174458-0413-89062590-p2m.xml',
                'blast.fasta')
