'''
Evaulate clusters
'''

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    DF = pd.read_table(
        './cd_hit_results/uniref90_100_90_against_homo_30/clusters/merged_clusters.fasta',
        sep=' ',
        names=['cluster', 'id', 'group', 'family', 'score'],
        index_col=1)
    IMG, AX1 = plt.subplots()
    CL0 = DF['score'][:6].values
    CL1 = DF['score'][6:11].values
    CL2 = DF['score'][11:15].values
    CL3 = DF['score'][15:20].values
    CL4 = DF['score'][20:23].values
    CL5 = DF['score'][23:27].values
    CL6 = DF['score'][27:32].values
    CL7 = DF['score'][32:34].values
    CL8 = DF['score'][34:36].values
    CL9 = DF['score'][36:39].values
    CL10 = DF['score'][39:41].values
    CL11 = DF['score'][41:42].values
    CL12 = DF['score'][42:43].values
    CL13 = DF['score'][43:44].values
    CL14 = DF['score'][44:46].values
    AX1.boxplot([CL0, CL1, CL2, CL3, CL4, CL5, CL6, CL7, CL8, CL9, CL10, CL11, CL12, CL13, CL14],)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
               ['RSK', 'DAPK', 'CAMK2', 'CAMK1', 'PDK', 'MLCK', 'MAPKAPK', 'Trio',
                'DCAMKL', 'CAMKL', 'PHK', 'PLK', 'RAD53', 'CAMK-Unique'], rotation=45)
    plt.savefig('./graphs/boxplots.png')
