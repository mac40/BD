'''
hmm evaluation via precision and recall table
'''

import sys

import matplotlib.pyplot as plt
import numpy as np
from Bio.SearchIO import parse
from sklearn.metrics import confusion_matrix


def parse_labelled_hmmout(file_name):
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

def parse_hmmout(file_name):
    '''
    parse an hmmsearch output and return an array with group, family and score\n
    INPUT: filename of the hmmsearch output\n
    OUTPUT: np.array [id]
    '''
    output = np.array([])
    for qresult in parse(file_name, 'hmmer3-tab'):
        for item in qresult.hits:
            if output.size == 0:
                output = np.array([int(item.bitscore), item.id.split('|')[1]])
            else:
                output = np.vstack([output, [int(item.bitscore), item.id.split('|')[1]]])
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

def sens_spec_acc(array, image):
    '''
    calculate sensitivity, specificity and accurancy for all possible trhesholds\n
    INPUT: array of values parsed with parse_hmmout,
    image = True or False if you want to print the graph or not\n
    OUTPUT: threshold value, if image = TRUE saves a graph in graphs folder
    '''
    sensitivity_ar = []
    specificity_ar = []
    accurancy_ar = []
    for trh in range(0, int(array[0][0])):
        cm_ = binary_confusion_matrix(array, trh)
        tn_ = cm_[0][0]
        fp_ = cm_[0][1]
        fn_ = cm_[1][0]
        tp_ = cm_[1][1]
        sensitivity_ar.append((tp_/(tp_+fn_)))
        specificity_ar.append((tn_/(tn_+fp_)))
        accurancy_ar.append(((tp_+tn_)/(tp_+tn_+fp_+fn_)))
    if image:
        fig_ = plt.figure()
        ax_ = fig_.add_subplot(1, 1, 1)
        _ = ax_.plot(sensitivity_ar, 'r', label='sensitivity')
        _ = ax_.plot(specificity_ar, 'g', label='specificity')
        _ = ax_.plot(accurancy_ar, 'b', label='accurancy')
        _ = ax_.axvline(accurancy_ar.index(max(accurancy_ar)))
        _ = ax_.legend(loc='best')
        fig_.savefig('./graphs/sens_spec_acc.png')
    return accurancy_ar.index(max(accurancy_ar))

if __name__ == "__main__":
    ARRAY = parse_labelled_hmmout(sys.argv[1])
    BEST_THRESHOLD = sens_spec_acc(ARRAY, False)
    print("best threshold = {}".format(BEST_THRESHOLD))
