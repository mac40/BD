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

    CLUSTERS = []
    for i in range(0, DF['cluster'][DF['group'] != '?'].max()+1):
        CLUSTERS.append(DF['score'].loc[DF['cluster'] == i].values)

    AX1.boxplot(CLUSTERS)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
               ['RSK', 'DAPK', 'CAMK2', 'CAMK1', 'PDK', 'MLCK', 'MAPKAPK', 'Trio',
                'DCAMKL', 'CAMKL', 'PHK', 'PLK', 'RAD53', 'CAMK-Unique'], rotation=45)
    plt.savefig('./graphs/boxplots.png')
