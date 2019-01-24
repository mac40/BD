'''
defining function to modify clustal omega results in order to remove columns
under certain threshold of conservation
'''

from Bio import AlignIO


ALIGN = AlignIO.read("./3_clustal_omega_results/muscle_uniref90_100.clw", "clustal")

REMOVABLE_COLS = []

for col in range(0, len(ALIGN[0])):
    gaps = 0
    for el in ALIGN[:, col]:
        if el == '-':
            gaps += 1
    if gaps > 20:
        REMOVABLE_COLS.append(col)

for col in reversed(REMOVABLE_COLS):
    ALIGN = ALIGN[:, :col-1] + ALIGN[:, col:]

AlignIO.write(ALIGN, "./4_parsed_clustal_omega_results/muscle_uniref90_100.clw", "clustal")
