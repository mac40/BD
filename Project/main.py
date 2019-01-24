'''
main python file
'''

import blast_parser as bp

if __name__ == "__main__":
    PROTEIN_LIST = bp.txt_to_protein_list("./1_blast_results/uniref90_ids.txt")
    bp.query_uniprotkb_uniref90(
        PROTEIN_LIST, './2_parsed_blast_results/uniref90_blast_100.fasta', 100)
