'''
split clusters in single fasta files
'''

import re
import sys
import urllib.request


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        BASE_URL = 'https://www.uniprot.org/uniprot/'
        EXTENSION = '.fasta'
        for line in infile:
            if re.match(r'>Cluster\s[0-9]*', line):
                if int(line[9:]) >= 1:
                    cluster.close()
                cluster = open(
                    'cd_hit_results/uniref90_100_90_against_homo_30/clusters/{}.fasta'.format(line[1:-1]), 'w')
            else:
                regex = re.search(r'[0-9]*\s[0-9]*aa,\s>[a-z]{2}\|(.*)\|.*', line)
                protein = regex.group(1)
                url = BASE_URL + protein + EXTENSION
                protein_fasta = urllib.request.urlopen(url).read()
                # cluster.write(protein_fasta.decode("utf-8"))
                cluster.write('{}\n'.format(protein))
    cluster.close()
