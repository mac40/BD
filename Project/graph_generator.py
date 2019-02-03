'''
General file for graph generation after completion of the work
'''

import numpy as np
import matplotlib.pyplot as plt

def disorder_content():
    '''
    disorder content graph
    '''
    values = [np.average([0.37583892617449666, 0.3724053724053724, 0, 0.19644723092998956]),
              np.average([0.062162162162162166, 0, 0, 0.1497584541062802, 0.15591397849462366]),
              np.average([0, 0.051351351351351354, 0, 0.032214765100671144, 0.1059850374064838, 0.08937823834196891]),
              np.average([0.12971698113207547, 0.06753246753246753]),
              np.average([0.06753246753246753, 0.12050739957716702, 0, 0.058823529411764705, 0.0728862973760933]),
              np.average([0.09011725293132328, 0.16176945431062317]),
              np.average([0.058577405857740586, 0, 0.27927927927927926, 0.14157706093189965]),
              np.average([0.0449438202247191, 0.02850877192982456, 0.12870159453302962]),
              np.average([0.1837837837837838, 0.2402088772845953]),
              np.average([0.34930139720558884, 0.24124513618677043]),
              np.average([0, 0]),
              np.average([0.10752688172043011, 0.15706806282722513, 0.1075, 0.17204301075268819, 0]),
              np.average([0.18232044198895028]),
              np.average([0.3086232980332829, 0.09302325581395349, 0.2213375796178344]),
              np.average([0.19690721649484536])]
    labels = ['MLCK', 'DAPK',
              'RSK', 'PSK', 'CAMK1', 'Trio', 'CAMK2',
              'PKD', 'DCAMKL', 'CAMK-Unique', 'PHK', 'MAPKAPK',
              'RAD53', 'CAMKL', 'Other PLK']

    fig, ax_ = plt.subplots()
    fig.subplots_adjust(bottom=0.3)
    _ = ax_.bar(labels, values)
    _ = ax_.set_xticklabels(labels, rotation=90)
    plt.savefig('./graphs/avg_disorder_content.png')

if __name__ == "__main__":
    disorder_content()
