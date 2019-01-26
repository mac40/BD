'''
hmm evaluation via precision and recall table
'''

import sys

import matplotlib.pyplot as plt
import numpy as np
from Bio.SearchIO import parse
from sklearn.metrics import confusion_matrix


def parse_hmmout(file_name):
    '''
    parse an hmmsearch output and return an array with group, family and score\n
    INPUT: filename of the hmmsearch output\n
    OUTPUT: np.array [group, family, score]
    '''
    output = np.array([])
    for qresult in parse(file_name, 'hmmer3-tab'):
        for item in qresult.hits:
            group = item.description.split()[1]
            family = item.description.split()[2]
            score = item.bitscore
            if output.size == 0:
                output = np.array([int(score), group, family])
            else:
                output = np.vstack([output, [int(score), group, family]])
    return output


def binary_confusion_matrix(hmmout, threshold):
    '''
    take as input the output of parse_hmmout and a threshold and returns a confusion\n
    matrix calculated on the binary equivalent of the input columns given a threshold\n
    INPUT: array of elements from hmmout, threshold\n
    OUTPUT: confusion_matrix, precision and recall
    '''
    y_true = []
    y_pred = []

    for row in hmmout:
        if int(row[0]) > int(threshold):
            y_pred.append(1)
        else:
            y_pred.append(0)
        if row[1] == "CAMK":
            y_true.append(1)
        else:
            y_true.append(0)
    return confusion_matrix(y_true, y_pred)


if __name__ == "__main__":
    ARRAY = parse_hmmout(sys.argv[1])
    SENSITIVITY_AR = []
    SPECIFICITY_AR = []
    ACCURANCY_AR = []
    for trh in range(0, int(ARRAY[0][0])):
        CM = binary_confusion_matrix(ARRAY, trh)
        TN = CM[0][0]
        FP = CM[0][1]
        FN = CM[1][0]
        TP = CM[1][1]
        SENSITIVITY = TP/(TP+FN)
        SPECIFICITY = TN/(TN+FP)
        ACCURANCY = (TP+TN)/(TP+TN+FP+FN)
        SENSITIVITY_AR.append(SENSITIVITY)
        SPECIFICITY_AR.append(SPECIFICITY)
        ACCURANCY_AR.append(ACCURANCY)
    FIG = plt.figure()
    AX = FIG.add_subplot(1, 1, 1)
    _ = AX.plot(SENSITIVITY_AR, 'r', label='sensitivity')
    _ = AX.plot(SPECIFICITY_AR, 'g', label='specificity')
    _ = AX.plot(ACCURANCY_AR, 'b', label='accurancy')
    _ = AX.axvline(ACCURANCY_AR.index(max(ACCURANCY_AR)))
    _ = AX.legend(loc='best')
    FIG.savefig('./graphs/sens_spec_acc.png')
    print("best threshold = {}".format(ACCURANCY_AR.index(max(ACCURANCY_AR))))
